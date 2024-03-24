class Generator:

    def __init__(self, name, bus, voltage, v_pu, p_set, q_set , q_min ,q_max , xg0, xg1, xg2, grounded, groundingZ):
        self.name=name
        self.bus=bus
        self.v_pu=v_pu
        self.voltage=voltage
        self.P=P_setpoint
        self.Q=Q_setpoint
        self.Q_min=Q_min
        self.Q_max=Q_max
        self.vControl=True
        self.zBaseOld=voltage**2/P_setpoint
        self.Xg1=Xg1
        self.Xg2=Xg2
        self.Xg0=Xg0
        self.grounded=grounded
        self.groundingZ=groundingZ    #ohms

    def set_p(self,p):
        self.p=p
    def set_q(self,q):
        self.q=q