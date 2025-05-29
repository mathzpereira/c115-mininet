from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI


class CustomTopo(Topo):
    def build(self):
        # Switches
        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")
        s5 = self.addSwitch("s5")

        # Hosts
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        h3 = self.addHost("h3")
        h4 = self.addHost("h4")
        h5 = self.addHost("h5")
        h6 = self.addHost("h6")
        h7 = self.addHost("h7")
        h8 = self.addHost("h8")

        # Links
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h5, s2)
        self.addLink(h3, s5)
        self.addLink(h4, s5)
        self.addLink(h6, s3)
        self.addLink(h7, s3)
        self.addLink(h8, s3)


if __name__ == "__main__":
    topo = CustomTopo()
    net = Mininet(topo=topo, cleanup=True, autoSetMacs=True)
    net.start()
    CLI(net)
    net.stop()
