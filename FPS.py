"""
Videojuego: First person shooter
Autor: José Emiliano Riosmena Castañón
"""
from pyexpat import model
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.health_bar import HealthBar

app = Ursina()

random.seed(0)

Entity.default_shader = lit_with_shadows_shader #Texturas sombreadas

suelo = Entity(model = 'plane', collider = 'box', scale = 200, texture = 'grass', texture_scale = (4, 4))
jugador = FirstPersonController(z = -10, origin_y = -0.5, speed = 8)
jugador.collider = BoxCollider(jugador, Vec3(0, 1, 0)) #Control de salto

pared1 = Entity(model = 'cube', texture = 'brick', collider = 'cube', scale = (200, 10, 5), position = (0, 5, 100), color = color.orange)
pared2 = duplicate(pared1, z= -100)
pared3 = duplicate(pared1, rotation_y = 90, x = -100, z = 0)
pared4 = duplicate(pared3, x = 100)

arma = Entity(model = 'cube', parent = camera, position = (0.5, -0.25, 0.25), scale = (0.3, 0.2, 1), origin_z = -0.5, color = color.black, on_cooldown=False)
disparo = Entity(parent = arma, z = 1, world_scale = 0.5, model = 'quad', color = color.gold, enabled = False)
disparos = Entity()

mouse.traverse_target = disparos

def update():
    if held_keys['left mouse']:
        arma.position = (0.45, -0.15, 0.15)
        disparar()
    else:
        arma.position = (0.5, -0.25, 0.25)

def disparar():
    if not arma.on_cooldown:
        arma.on_cooldown = True
        arma.position = (0.45, -0.15, 0.15)
        disparo.enabled = True
        invoke(disparo.disable, delay = 0.05)
        invoke(setattr, arma, 'on_cooldown', False, delay = 0.15)
        if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'salud'):
            mouse.hovered_entity.salud -= 10
            mouse.hovered_entity.blink(color.red)

class Enemigo(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent = disparos, model = 'cube', scale_y = 2, origin_y = -0.5, color = color.light_gray, collider = 'box', **kwargs)
        self.barra_salud = Entity(parent = self, y = 1.2, model = 'cube', color = color.red, world_scale = (1.5, 0.1, 0.1))
        self.max_salud = 100
        self.salud = self.max_salud

    def update(self):
        distancia = distance_xz(jugador.position, self.position)
        if distancia > 40:
            return
        self.barra_salud.alpha = max(0, self.barra_salud.alpha - time.dt)

        self. look_at_2d(jugador.position, 'y')
        golpe = raycast(self.world_position + Vec3(0, 1, 0), self.forward, 30, ignore = (self,))
        if golpe.entity == jugador:
            if distancia > 2:
                self.position += self.forward * time.dt * 5
        
    @property
    def salud(self):
        return self._salud

    @salud.setter
    def salud(self, valor):
        self._salud = valor
        if valor <= 0:
            destroy(self)
            return
        self.barra_salud.world_scale_x = self.salud / self.max_salud * 1.5
        self.barra_salud.alpha = 1

enemigos = [Enemigo(x = x * 20) for x in range(20)]
sol = DirectionalLight()
sol.look_at(Vec3(1, -1, -1))
Sky()

app.run()
