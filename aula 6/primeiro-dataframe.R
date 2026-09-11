# Primeiro Data frame
df_teste <- data.frame(
  nome = c("Bob", "Mel", "Dan", "Tom", "Kian"),
  idade = c(12, 13, 14, 15, 4000),
  salario = c(1000.1, 1000.2, 1000.3, 1000.4, 50000.12)
)

df_teste$idade
mean(df_teste$idade)
head(df_teste)
str(df_teste)
dim(df_teste)
median(df_teste$idade)

summary(df_teste)
df_teste$ganha_bem <- NULL #Deleta a coluna
df_teste$ganha_bem <- df_teste$salario > 1400

df_teste$ganha_bem <- ifelse(df_teste$salario > 1400, "Sim", "Não")

?ifelse # ? abre a documentação


df_teste[2,2]
df_teste[2,]
df_teste[,2]
df_teste[df_teste$idade>30,]