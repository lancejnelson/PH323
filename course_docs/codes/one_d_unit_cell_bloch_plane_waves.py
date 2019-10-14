#!/usr/bin/env python


class basisExpansion:

    def __init__(self,bounds,dx,atomLocations,wellWidth,nBasis,V):
        from numpy import arange,where,zeros_like
                #self.x = arange(-L/2,L/2,dx)
        self.dx = dx
        self.bounds = bounds
        self.a = bounds[1] - bounds[0]
        self.x = arange(bounds[0] ,bounds[1]+dx,dx)
        self.atomLocations = atomLocations
        self.nAtoms = len(atomLocations)
        self.wellWidth = wellWidth
        self.nBasis = nBasis
        #self.V = - abs(5/(self.x - self.atomLocations[0])) - abs(5/(self.x - self.atomLocations[0] + self.a))- abs(5/(self.x - self.atomLocations[0] - self.a))- abs(5/(self.x - (self.atomLocations[0] + 2 * self.a)))#- abs(5/(self.x + self.atomLocations[0] + 3 * self.a))
        #self.V[self.V < -100] = -100        
        self.V = zeros_like(self.x)
        for iatom,atom in enumerate(self.atomLocations):
            self.V[(self.x > atom - self.wellWidth/2) & (self.x < atom + self.wellWidth/2)] = V[iatom]
        
    def basis(self,n,k,x):
        from numpy import sin,pi,sqrt,exp
        basis =1/sqrt(self.a ) * exp( complex(0,1) * ( 2 * pi * n  * x/self.a + k * x))
        return basis


    def plotbasis(self,n):
        from matplotlib import pyplot
        from numpy import linspace
        x = linspace(-self.L/2,self.L/2,1000)
        pyplot.plot(x,self.basis(n,x))
        pyplot.show()


    def DDbasis(self,n,k,x):
        from numpy import pi,sqrt,sin,exp
        ddbas = 1/sqrt(self.a ) *complex(0,1)**2 * (2 * pi * n  /self.a + k)**2 * exp( complex(0,1) * (2 * pi * n  * x/self.a + k * x))
        return ddbas

    
    def plotV(self):
        from matplotlib import pyplot
        pyplot.plot(self.x,self.V)
        pyplot.show()

    def HamiltonianMatrix(self,k):
        self.k = k
        print("building Hamiltonian Matrix",self.k)
        from numpy import zeros,set_printoptions
        self.H = zeros([self.nBasis+1,self.nBasis+1],dtype = complex)
        for iindex,ibas in enumerate(range(-self.nBasis//2,self.nBasis//2+1)):
            for jindex,jbas in enumerate(range(-self.nBasis//2,self.nBasis//2+1)):
                self.H[iindex,jindex] = self.dx * sum(self.basis(ibas,self.k,self.x).conjugate() * self.V * self.basis(jbas,self.k,self.x)) + self.KE(ibas,jbas)
    def KE(self,ibas,jbas):
        return  -self.dx * sum(self.basis(ibas,self.k,self.x).conjugate() * self.DDbasis(jbas,self.k,self.x))

    def solveProblem(self):
        from numpy.linalg import eig
        print("Solving Problem")
        vals,self.vecs = eig(self.H)
        self.sortkey = sorted(range(self.nBasis),key = lambda x:vals[x])
        self.vals = sorted(vals)
        print("The lowest eigenvalue for k = {} is {}".format(self.k,self.vals[:3]))

    def plotSolution(self,n):
        print("Plotting Solution")
        from numpy import zeros_like,cos,sin
        solVec = self.vecs[:,self.sortkey[n]]
        plotx,dx = linspace(0,2 * self.a,1000,retstep = True)
        gsWaveFunc =zeros_like(plotx,dtype = complex)
        for iindex, ibas in enumerate(range(-self.nBasis//2,self.nBasis//2 +1 )):
            gsWaveFunc += solVec[iindex] * self.basis(ibas,self.k,plotx)
        normalization = dx *sum(gsWaveFunc.conjugate() * gsWaveFunc)    
        pyplot.figure(1)
        pyplot.plot(plotx, 1/normalization * gsWaveFunc.conjugate() * gsWaveFunc,'r--',linewidth=3.4,label='square of wave function')
        pyplot.plot(self.x,self.V,'b--',linewidth=3.4)
        pyplot.ylim(-1,max(gsWaveFunc.conjugate() * gsWaveFunc))
        pyplot.title("k = {}. pi/a = {}".format(self.k,pi/self.a))
        pyplot.legend()
        pyplot.grid(True,linestyle = '--')
        pyplot.show()
    

from numpy import linspace,zeros,arange,pi
from matplotlib import pyplot,rc
rc('text',usetex=True)

nBasis = 5
dx = .001
bounds = [0,3]  #Unit cell in one dimension
atomLocations = [1.5] # Where are the potentials going to be located
nAtoms = len(atomLocations)
V = [-20]
wellWidth =1  # How wide are the potential wells?  They are just square wells
k =  pi/ 3/2
myBasisExpansion = basisExpansion(bounds,dx,atomLocations,wellWidth,nBasis,V)


myBasisExpansion.plotV()
myBasisExpansion.HamiltonianMatrix(k)
myBasisExpansion.solveProblem()
myBasisExpansion.plotSolution(0)
myBasisExpansion.plotSolution(1)
myBasisExpansion.plotSolution(2)

