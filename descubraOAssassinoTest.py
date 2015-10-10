import descubraOAssassino
import unittest

class Test(unittest.TestCase):	

	def testTeoria(self):
		test = descubraOAssassino.Jogo()		
		self.assertEqual(test.teoria(),[1,1,1])

	def testTeoria2(self):
		test = descubraOAssassino.Jogo()
		test.suspeitos = test.suspeitos[2:]
		test.locais = test.locais[2:]
		test.armas = test.armas[2:]
		self.assertEqual(test.teoria(),[3,3,3])

	def testTrataResposta1(self):
		test = descubraOAssassino.Jogo()
		suspeitosAux = test.suspeitos[1:]
		test.trataResposta(1)
		self.assertEqual(test.suspeitos, suspeitosAux)

	def testTrataResposta2(self):
		test = descubraOAssassino.Jogo()
		locaisAux = test.locais[1:]
		test.trataResposta(2)
		self.assertEqual(test.locais, locaisAux)

	def testTrataResposta3(self):
		test = descubraOAssassino.Jogo()
		armasAux = test.armas[1:]
		test.trataResposta(3)
		self.assertEqual(test.armas, armasAux)

	def testJogarDevePedirNovoJogo(self):
		global novoJogoChamado
		novoJogoChamado = False
		def mockNovoJogo():
			global novoJogoChamado
			novoJogoChamado = True

		descubraOAssassino.assassino.novoJogo = mockNovoJogo
		test = descubraOAssassino.Jogo()
		test.jogar()
		self.assertTrue(novoJogoChamado)

	def testSequenciaFatos(self):		
		global callCounter
		callCounter = 0
		def mockNovoJogo():			
			global callCounter
			callCounter += 1
			self.assertEqual(callCounter, 1)
		def mockTentativa(nada):		
			global callCounter
			callCounter += 1
			if(callCounter >= 4):
				return 0
			self.assertEqual(callCounter, 3)

		descubraOAssassino.assassino.novoJogo = mockNovoJogo
		descubraOAssassino.assassino.tentativa = mockTentativa
		test = descubraOAssassino.Jogo()				

		def mockTeoria():		
			global callCounter
			callCounter +=1 
			if(callCounter >= 4):
				return 0
			self.assertEqual(callCounter, 2)
		def mockTrataResposta(nada):		
			global callCounter
			callCounter += 1
			self.assertEqual(callCounter, 4)

		test.teoria = mockTeoria
		test.trataResposta = mockTrataResposta
		test.jogar()
