from animal_types import Ant, Copperhead, Earthworm, Finch, Fish, Gerbil, Mouse, Parakeet, Rattlesnake, Terrapin
from containers import Aboveground, Aquarium, Aviary, Underground

cage = Aboveground("cage")
tank = Aquarium("tank")
dome = Aviary("dome")
tunnel = Underground("tunnel")

andrew = Ant("Andrew")
cooper = Copperhead("Cooper")
eric = Earthworm("Eric")
finly = Finch("Finly")
felicia = Fish("Felicia")
george = Gerbil("George")
moses = Mouse("Moses")
pat = Parakeet("Pat")
ralph = Rattlesnake("Ralph")
ted = Terrapin("Ted")

cage.add_animal(andrew)
tank.add_animal(andrew)
dome.add_animal(andrew)
tunnel.add_animal(andrew)
andrew.action()

cage.add_animal(cooper)
tank.add_animal(cooper)
dome.add_animal(cooper)
tunnel.add_animal(cooper)
cooper.action()

cage.add_animal(eric)
tank.add_animal(eric)
dome.add_animal(eric)
tunnel.add_animal(eric)
eric.action()

cage.add_animal(finly)
tank.add_animal(finly)
dome.add_animal(finly)
tunnel.add_animal(finly)
finly.action()

cage.add_animal(felicia)
tank.add_animal(felicia)
dome.add_animal(felicia)
tunnel.add_animal(felicia)
felicia.action()

cage.add_animal(george)
tank.add_animal(george)
dome.add_animal(george)
tunnel.add_animal(george)
george.action()

cage.add_animal(moses)
tank.add_animal(moses)
dome.add_animal(moses)
tunnel.add_animal(moses)
moses.action()

cage.add_animal(pat)
tank.add_animal(pat)
dome.add_animal(pat)
tunnel.add_animal(pat)
pat.action()

cage.add_animal(ralph)
tank.add_animal(ralph)
dome.add_animal(ralph)
tunnel.add_animal(ralph)
ralph.action()

cage.add_animal(ted)
tank.add_animal(ted)
dome.add_animal(ted)
tunnel.add_animal(ted)
ted.action()
