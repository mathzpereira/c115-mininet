# Trabalho de Redes com Mininet

## Exercício 1 - Topologia Árvore com Profundidade Quatro e Ramificação três

### a) Criação da Topologia

Com uso de linha de comando padrão do Mininet, crie a topologia considerando o endereço MAC padronizado, larguras de banda bw de 35Mbps e controlador do Mininet (não precisa especificar):

```bash
sudo mn --topo=tree,depth=4,fanout=3 --mac --link ovs,bw=35
```

---

### b) Inspeção das Interfaces

Inspecione informações das interfaces, endereços MAC, IP e portas através de linhas de comando:

- Ver a lista de nós disponíveis na topologia:

```bash
nodes
```

- Ver a conexão entre os nós (hosts e switches):

```bash
net
```

- Ver endereços IP e MAC de um host:

```bash
h1 ifconfig -a
```

- Ver interfaces de um switch:

```bash
s1 ifconfig -a
```

---

### c) Informações da Topologia

Crie um desenho ilustrativo da topologia com todas as 
informações obtidas no item anterior:

- A topologia possui 40 switches, 81 hosts e vários links. Seria inviável criar um desenho para representar essa topologia tão grande, mas abaixo está a resposta do terminal que comprova essas informações.

```bash
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Adding links:
(s1, s2) (s1, s15) (s1, s28) (s2, s3) (s2, s7) (s2, s11) (s3, s4) (s3, s5) (s3, s6) (s4, h1) (s4, h2) (s4, h3) (s5, h4) (s5, h5) (s5, h6) (s6, h7) (s6, h8) (s6, h9) (s7, s8) (s7, s9) (s7, s10) (s8, h10) (s8, h11) (s8, h12) (s9, h13) (s9, h14) (s9, h15) (s10, h16) (s10, h17) (s10, h18) (s11, s12) (s11, s13) (s11, s14) (s12, h19) (s12, h20) (s12, h21) (s13, h22) (s13, h23) (s13, h24) (s14, h25) (s14, h26) (s14, h27) (s15, s16) (s15, s20) (s15, s24) (s16, s17) (s16, s18) (s16, s19) (s17, h28) (s17, h29) (s17, h30) (s18, h31) (s18, h32) (s18, h33) (s19, h34) (s19, h35) (s19, h36) (s20, s21) (s20, s22) (s20, s23) (s21, h37) (s21, h38) (s21, h39) (s22, h40) (s22, h41) (s22, h42) (s23, h43) (s23, h44) (s23, h45) (s24, s25) (s24, s26) (s24, s27) (s25, h46) (s25, h47) (s25, h48) (s26, h49) (s26, h50) (s26, h51) (s27, h52) (s27, h53) (s27, h54) (s28, s29) (s28, s33) (s28, s37) (s29, s30) (s29, s31) (s29, s32) (s30, h55) (s30, h56) (s30, h57) (s31, h58) (s31, h59) (s31, h60) (s32, h61) (s32, h62) (s32, h63) (s33, s34) (s33, s35) (s33, s36) (s34, h64) (s34, h65) (s34, h66) (s35, h67) (s35, h68) (s35, h69) (s36, h70) (s36, h71) (s36, h72) (s37, s38) (s37, s39) (s37, s40) (s38, h73) (s38, h74) (s38, h75) (s39, h76) (s39, h77) (s39, h78) (s40, h79) (s40, h80) (s40, h81)
```
---

### d) Testes de Conectividade (Ping)

Execute testes de ping entre os diferentes nós, mostre 
os pacotes chegando nos nós com uso do comando 
tcpdump:

- Ping entre todos os nós automaticamente:

```bash
pingall
```

- Abrir um terminal para o h2 (xterm h2) e executar o tcpdump:

```bash
tcpdump -i h2-eth0 -nn icmp
```

---

### e) Teste de Desempenho com iPerf

Especifique que o host 1 na porta 5555 vai ser um servidor TCP e o host 2 um cliente e execute testes de iperf, considere um relatório por segundo com teste de 20 segundos. Faça os testes para larguras de banda bw de 5, 10, 25 e 35 Mbps (Necessário reconstruir a topologia para os outros valores).

- Especifique o **host 1 (h1)** como servidor TCP na porta **5555**:

```bash
h1 iperf -s -p 5555 -i 1
```

- Especifique o **host 2 (h2)** como cliente, conectando-se ao servidor, com relatório a cada 1 segundo por 20 segundos:

```bash
h2 iperf -c 10.0.0.2 -p 5555 -i 1 -t 20
```

OBS: Para reconstruir a topologia com as diferentes larguras de banda, deve ser executado o comando abaixo apenas alterando o valor de bw.

```bash
sudo mn --topo=tree,depth=4,fanout=3 --mac --link ovs,bw=[5, 10, 25, 35]
```

---

## Exercício 2 - Topologia Customizada em Python

### a) Criação da Topologia

Com uso de linha de comando padrão do Mininet, crie a topologia customizada considerando o endereço MAC padronizado e controlador manual:

```shell
sudo python3 topologia.py
```

---

### b) Inspeção das Interfaces

Inspecione informações das interfaces, endereços MAC, IP e portas através de linhas de comando:

```shell
mininet> nodes
available nodes are:
c0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s5

mininet> net
h1 h1-eth0:s1-eth1
h2 h2-eth0:s2-eth1
h3 h3-eth0:s5-eth1
h4 h4-eth0:s5-eth2
h5 h5-eth0:s2-eth2
h6 h6-eth0:s3-eth1
h7 h7-eth0:s3-eth2
h8 h8-eth0:s3-eth3
s1 lo:  s1-eth1:h1-eth0
s2 lo:  s2-eth1:h2-eth0 s2-eth2:h5-eth0
s3 lo:  s3-eth1:h6-eth0 s3-eth2:h7-eth0 s3-eth3:h8-eth0
s5 lo:  s5-eth1:h3-eth0 s5-eth2:h4-eth0
c0

mininet> dump
<Host h1: h1-eth0:10.0.0.1 pid=4840>
<Host h2: h2-eth0:10.0.0.2 pid=4842>
<Host h3: h3-eth0:10.0.0.3 pid=4844>
<Host h4: h4-eth0:10.0.0.4 pid=4846>
<Host h5: h5-eth0:10.0.0.5 pid=4848>
<Host h6: h6-eth0:10.0.0.6 pid=4850>
<Host h7: h7-eth0:10.0.0.7 pid=4852>
<Host h8: h8-eth0:10.0.0.8 pid=4854>
<OVSSwitch s1: lo:127.0.0.1,s1-eth1:None pid=4859>
<OVSSwitch s2: lo:127.0.0.1,s2-eth1:None,s2-eth2:None pid=4862>
<OVSSwitch s3: lo:127.0.0.1,s3-eth1:None,s3-eth2:None,s3-eth3:None pid=4865>
<OVSSwitch s5: lo:127.0.0.1,s5-eth1:None,s5-eth2:None pid=4868>
<Controller c0: 127.0.0.1:6653 pid=4833>

```
---

### c) Informações da Topologia

Crie um desenho ilustrativo da topologia com todas as informações obtidas no item anterior:

```plaintext
H1      H2      H5       H3     H4
 |       |       |        |      |
S1 ----- S2 ----- S5 -----+------+ 
         |
         +----- S3
                 | \
                H6 H7 H8
```

---

### d) Testes de Conectividade (Ping)

Faça testes de ping considerando os switches normais:

```shell
mininet> pingall
*** Ping: testing ping reachability
h1 -> X X X X X X X
h2 -> X X X h5 X X X
h3 -> X X h4 X X X X
h4 -> X X h3 X X X X
h5 -> X h2 X X X X X
h6 -> X X X X X h7 h8
h7 -> X X X X X h6 h8
h8 -> X X X X X h6 h7
*** Results: 82% dropped (10/56 received)
```

### e) Alterar regras

Apague as regras anteriores e crie regras baseadas em endereços MAC para alguns nós. (Deve-se comunicar hosts dos diferentes switches):

```shell
sh ovs-ofctl del-flows s1
```

Para permitir a comunicação entre o par h1 (conectado a s1) <-> h6 (conectado a s3):

```shell
mininet> sh ovs-ofctl add-flow s1 "priority=10,in_port=1,dl_src=00:00:00:00:00:01,actions=output:2"
mininet> sh ovs-ofctl add-flow s1 "priority=10,in_port=2,dl_dst=00:00:00:00:00:01,actions=output:1"
mininet> sh ovs-ofctl add-flow s2 "priority=10,in_port=1,dl_dst=00:00:00:00:00:06,actions=output:4"
mininet> sh ovs-ofctl add-flow s2 "priority=10,in_port=4,dl_dst=00:00:00:00:00:01,actions=output:1"
mininet> sh ovs-ofctl add-flow s3 "priority=10,in_port=2,dl_src=00:00:00:00:00:06,actions=output:1"
mininet> sh ovs-ofctl add-flow s3 "priority=10,in_port=1,dl_dst=00:00:00:00:00:06,actions=output:2"
```

### f) Novos testes de ping

Faça testes de ping para demonstrar que as regras foram bem implementadas:

```shell
mininet> h1 ping -c 3 h6
PING 10.0.0.6 (10.0.0.6) 56(84) bytes of data.
64 bytes from 10.0.0.6: icmp_seq=1 ttl=64 time=2.05 ms
64 bytes from 10.0.0.6: icmp_seq=2 ttl=64 time=1.89 ms
64 bytes from 10.0.0.6: icmp_seq=3 ttl=64 time=0.499 ms

--- 10.0.0.6 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2000ms
rtt min/avg/max/mdev = 0.499/1.482/2.054/0.698 ms
```