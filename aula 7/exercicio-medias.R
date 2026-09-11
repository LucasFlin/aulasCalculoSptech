
# As notas são parecidas entre os alunos ou muito diferentes?
# Existem notas parecidas, mas em geral a mediana varia bastante, principalmente na Entrega 3

#  Existe alguma entrega com maior variação de notas?
# A terceira entrega possui media e mediana menor que as demais

#  A média representa bem os dados em todos os casos?
# Sim, já que a média e a mediana apresentam uma diferença muito pequena nos 3 casos, presumo que elas não diferem muito.

#  O desvio padrão ajuda a entender o comportamento das notas? Como?
#Sim, o baixo desvio padrão mostra consistencia entre os dados

#  Existe alguma evidência de distribuição normal? Justifique com base nos gráficos.
# O gráfico da terceira entrega demontra um padrão de distribuição normal, apesar de assimetrica. 



valor_por_pedido <- round(rnorm(500, mean = 100, sd = 10),1) # Amostra "randomica" que se comporta como uma distribuição normal
hist(valor_por_pedido)
valor_por_pedido
sd(valor_por_pedido)

mediana1 = median(entregas.ccoa$Entrega.01)
mediana2 = median(entregas.ccoa$Entrega.02)
mediana3 = median(entregas.ccoa$Entrega.03)

media1 = mean(entregas.ccoa$Entrega.01)
media2 = mean(entregas.ccoa$Entrega.02)
media3 = mean(entregas.ccoa$Entrega.03)

desvio1 = sd(entregas.ccoa$Entrega.01)
desvio2 = sd(entregas.ccoa$Entrega.02)
desvio3 = sd(entregas.ccoa$Entrega.03)

hist(entregas.ccoa$Entrega.01)
abline(v = media1, col = "#121212", lwd = 2)
abline(v = mediana1, col = "#254254", lwd = 2)

hist(entregas.ccoa$Entrega.02)
abline(v = media2, col = "#121212", lwd = 2)
abline(v = mediana2, col = "#254254", lwd = 2)

hist(entregas.ccoa$Entrega.03)
abline(v = media3, col = "#121212", lwd = 2)
abline(v = mediana3, col = "#254254", lwd = 2)

# Qual entrega teve maior média?
# Entrega 2, com 8.84

#  Qual teve maior desvio padrão?
# Entrega 3, com 1.88


# Em qual atividade os alunos tiveram melhor desempenho?
# Entrega 2, pois além da média e mediana serem maiores, ela possui o menor desvio

# Em qual houve maior dificuldade ou desigualdade?
# Entrega 3, pois ela possui um intervalo maior entre os valores



entregas.ccoa$media.aluno <- (entregas.ccoa$Entrega.01+entregas.ccoa$Entrega.02+entregas.ccoa$Entrega.03)/3

# Aluno com maior média
aluno_maior_media <- entregas.ccoa[which.max(entregas.ccoa$media.aluno),]$RA

# Aluno com menor média
aluno_menor_media <- entregas.ccoa[which.min(entregas.ccoa$media.aluno),]$RA

hist(entregas.ccoa$media.aluno)

# Extra 
medianaTotal <- median(entregas.ccoa$media.aluno)
mediaTotal <- mean(entregas.ccoa$media.aluno)
abline(v = mediaTotal, col = "#121212", lwd = 2)
abline(v = medianaTotal, col = "#254254", lwd = 2)
# Creio que ainda não exista uma distribuição normal, mas a maior parte das medias ficou entre 8 e 9
#e a média e mediana estão relativamente distantes, indicando uma certa desigualdade entre os dados
