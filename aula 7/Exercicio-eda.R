media_ram <- aggregate(ram... ~ Nome, data = dados_todas_maquinas, FUN = mean)

usuario_mais_ram <-  dados_todas_maquinas[which.max(dados_todas_maquinas$ram...),]$Nome #Maquina com maior pico de uso de RAM
usuario_menos_ram <-  dados_todas_maquinas[which.min(dados_todas_maquinas$ram...),]$Nome #Maquina com maior pico de uso de RAM

dados_todas_maquinas$ram.status <- ifelse(dados_todas_maquinas$ram... < 50, "Boa", "Ruim")

barplot((table(dados_todas_maquinas$ram.status))) # Aqui podemos ver que as máquinas analizadas estão com um uso de RAM bem elevado
barplot((table(dados_todas_maquinas$Nome))) # Aqui podemos ver a máquina que coletou mais dados

plot(dados_todas_maquinas$cpu.total..., dados_todas_maquinas$ram...)
# Atravez deste plot podemos ver que todos os computadores possuem dados bem diferentes, mas em sua maioria uso de RAM elevado não parece ter relação com o uso de CPU
hist(dados_todas_maquinas$ram..., main = "RAM total", xlab = "RAM(%)", ylab = "Uso", col = "#03C8FF")
# Como podemos ver, a maior parte das máquinas registradas nesse periodo estão utilizando entre 80-85% de RAM