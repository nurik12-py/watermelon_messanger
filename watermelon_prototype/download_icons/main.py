import requests

icon_list = "alligator, anteater, armadillo, auroch, axolotl, badger, bat, beaver, buffalo, camel, chameleon, cheetah, chipmunk, chinchilla, chupacabra, cormorant, coyote, crow, dingo, dinosaur, dolphin, duck, dragon, elephant, ferret, fox, frog, giraffe, gopher, grizzly, hedgehog, hippo, hyena, jackal, ibex, ifrit, iguana, koala, kraken, lemur, leopard, liger, llama, manatee, mink, monkey, narwhal, nyan cat, orangutan, otter, panda, penguin, platypus, python, pumpkin, quagga, rabbit, raccoon, rhino, sheep, shrew, skunk, slow loris, squirrel, turtle, walrus, wolf, wolverine, wombat".split(
    ", ")

#for i in range(30):
#    response = requests.get(
#        "https://ssl.gstatic.com/docs/common/profile/" + icon_list[i] + "_lg.png")
#    file = open("icons/" + icon_list[i] + ".png", "wb")
#    file.write(response.content)
#    file.close()

print(icon_list[:30])
