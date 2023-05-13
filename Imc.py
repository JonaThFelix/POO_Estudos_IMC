class Imc:
  
  def __init__(self,nome,altura,peso):
    self.nome = nome
    self.altura = altura
    self.peso = peso

  def apresentar(self):
    print(f'Paciente: {self.nome}\nAltura:{self.altura:.2f} m\nPeso:{self.peso} Kg')

  def calc_imc(self):
    varimc = (self.peso)/self.altura**2 #declaraçã de variável para evitar chamar fórmula
    if varimc < 18.5:
      print(f'{self.nome} está ABAIXO do peso\nIMC: {varimc:.2f}.\nClassificação: Magreza\nObesidade:Grau: 0\nRecomendações: Proucure um médico/Nutricionista')
      
    if varimc > 18.5 and varimc < 24.9:
      print(f'{self.nome} está com peso NORMAL\nIMC {varimc:.2f}.\nClassificação: Normal\nObesidade: Grau: 0\nRecomendações: Continue assim.')

    if varimc > 25 and varimc < 29.9:
      print(f'{self.nome} está com SOBREPESO\nIMC {varimc:.2f}.\nClassificação: Sobrepeso\nObesidade: Grau I\nRecomendações: Cuidado com os hábitos e a alimentação')

    if varimc > 30 and varimc < 39.9:
      print(f'{self.nome} está com OBESIDADE\nIMC {varimc:.2f}. \nClassificação: Obesidade\nObesidade: Grau II\nRecomendações: Proucure um profissional e faça um acompanhamento')

    if varimc > 39.9:
      print(f'{self.nome} está com OBESIDADE GRAVE\n {varimc:.2f}. \nClassificação: Obesidade Grave\nObesidade: Grau III\nRecomendações: Proucure um médico Imediatamente !!!')
