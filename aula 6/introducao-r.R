a <- 2
b <- 40
if (a<b){
  "teste1"
}else{
  "teste2"
}

somar <- function(n1, n2){
  cat(n1+n2)
}

somar(a, b)

rm(b)

nomes <- c("Tom", "Bob", "Ana", "Dan")

for (nome in nomes){
  cat(nome, "\n")
}
