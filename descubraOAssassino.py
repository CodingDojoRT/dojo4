import random
import assassino

class Jogo:

	def __init__(self):
		self.suspeitos = [1,2,3,4,5,6]
		self.locais = [1,2,3,4,5,6,7,8,9,10]
		self.armas = [1,2,3,4,5,6]

	def teoria(self):
		return [self.suspeitos[0], self.locais[0], self.armas[0]]

	def trataResposta(self, resp):
		if(resp == 1):
			self.suspeitos.pop(0)
		elif(resp == 2):
			self.locais.pop(0)
		elif(resp == 3):
			self.armas.pop(0)

	def jogar(self):
		assassino.novoJogo()
		def passo():
			thisTeoria = self.teoria()
			print 'vou tentar essa porra: ' + str(thisTeoria)
			resp = assassino.tentativa(thisTeoria)
			print 'e tive essa resposta:' + str(resp)
			if resp is 0:
				return
			self.trataResposta(resp)
			passo()
		passo()

joguin = Jogo()
joguin.jogar()
joguin = Jogo()
joguin.jogar()
joguin = Jogo()
joguin.jogar()
joguin = Jogo()
joguin.jogar()
joguin = Jogo()
joguin.jogar()
joguin = Jogo()
joguin.jogar()













