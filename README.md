<div align="center">
  <a href="https://seu-link-de-download-aqui" target="_blank" style="text-decoration: none;">
    <div style="background: #0a0a0a; padding: 25px 40px; border-radius: 16px; display: inline-block; border: 3px solid #0f0; box-shadow: 0 0 35px rgba(0, 255, 0, 0.4); position: relative; overflow: hidden;">
      
      <!-- Efeito de scanline / CRT -->
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: repeating-linear-gradient(transparent 0px, transparent 2px, rgba(0,255,0,0.03) 2px, rgba(0,255,0,0.03) 4px); pointer-events: none; border-radius: 13px;"></div>
      
      <!-- Relógio Digital -->
      <div id="digital-clock" 
           style="font-family: 'Courier New', monospace; 
                  font-size: 92px; 
                  font-weight: bold; 
                  color: #00ff00; 
                  text-shadow: 
                    0 0 10px #00ff00,
                    0 0 20px #00ff00,
                    0 0 40px #00ff00;
                  letter-spacing: 8px;
                  background: rgba(0, 0, 0, 0.7);
                  padding: 10px 30px;
                  border-radius: 8px;
                  border: 2px solid #003300;">
        88:88:88
      </div>

      <div style="margin-top: 12px; display: flex; justify-content: space-between; align-items: center; color: #00cc00; font-family: monospace;">
        <span style="font-size: 18px;">● LIVE</span>
        <span id="date" style="font-size: 18px;"></span>
        <span style="font-size: 18px;">v1.2</span>
      </div>
    </div>
  </a>
</div>

<script>
// Atualiza relógio digital + data
function updateDigitalClock() {
  const now = new Date();
  
  let hours = String(now.getHours()).padStart(2, '0');
  let minutes = String(now.getMinutes()).padStart(2, '0');
  let seconds = String(now.getSeconds()).padStart(2, '0');
  
  document.getElementById('digital-clock').textContent = `${hours}:${minutes}:${seconds}`;
  
  // Data
  const options = { weekday: 'short', day: '2-digit', month: 'short' };
  document.getElementById('date').textContent = now.toLocaleDateString('pt-BR', options).toUpperCase();
}

setInterval(updateDigitalClock, 1000);
updateDigitalClock();
</script>

# 🕒 Relogio-flutuante
[![Versão](https://img.shields.io/github/v/release/Nyne1155/Relogio-flutuante)](https://github.com/Nyne1155/Relogio-flutuante/releases)
![Downloads](https://img.shields.io/github/downloads/Nyne1155/Relogio-flutuante/total)
[![Licença](https://img.shields.io/github/license/Nyne1155/Relogio-flutuante)](https://github.com/Nyne1155/Relogio-flutuante/blob/main/LICENSE)

![Screenshot](versoes/1.0.0/img.png)

RELOGIO flutuante v1.0.1
[RELOGIO v1.0.1.zip](https://github.com/user-attachments/files/29105475/RELOGIO.v1.0.0.zip)
NOVA VERSÃO!
- Corrigido um bug de crash inesperado que acontecia durante a inicialização da versão 1.0.0
- Estabilidade e desempenho melhorados.
- Atualização recomendada para todos os usuários.
Novas versões serão lançadas em breve :)

## 💻Compatibilidade
Este projeto foi testado e funciona corretamente em:
- **Windows** (todas as versões recentes)

## 📥 Download
![GitHub release](https://img.shields.io/github/v/release/Nyne1155/Relogio-flutuante)
[![Versão](https://img.shields.io/badge/Versão-v1.0.1-blue)](https://github.com/Nyne1155/Relogio-flutuante/releases/tag/v1.0.1)
![Stars](https://img.shields.io/github/stars/Nyne1155/Relogio-flutuante)

## ✨ Recursos

- ✅ Relógio em tempo real
- ✅ Janela flutuante
- ✅ Baixo consumo de memória
- ✅ Inicialização rápida
- 🚧 Temas personalizados
- 🚧 Transparência avançada

## 📜 Changelog

### v1.0.1
- Corrigido crash na inicialização
- Melhorias de desempenho

### v1.0.0
- Primeira versão pública

criado por: nyne1155
