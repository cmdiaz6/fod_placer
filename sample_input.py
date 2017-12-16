#IDEAS FOR NEW FUNCTIONALITY

#ORBITALS
type: 1s, sp3(methane?), Ne, Ar, Kr
e.g. 
#place at location
 1s a1 a2 a3 
#neon tetrahedra centered at a pointed towards b
# optional: align one point with point c
 sp3 ax ay az point bx by bz
 Ne ax ay az point bx by bz align cx cy cz
             pointback (spin down?)

#BONDS
bonds: db, tb #double bond, triple bond
e.g.
#double bond centered between a and b
# above and below plane defined by c
 db a1 a2 a3 to b1 b2 b3 plane c1 c2 c3
#linear atom: no plane
 db a1 a2 a3 to b1 b2 b3 noplane

#triple bond. how to define?
 tb a1 a2 a3 to b1 b2 b3 plane??

#C-H bond: default 0.085 Angstrom from carbon
 ch a... to b... (optional: dist d)

#BENZENE RING
 #carbons only
 # \   c  
 #  b/   \\d
 # ||      |
 #  a\     f
 # /   g//
 ring a b c d e f g
 #for polycenes. connect at 2 atom positions a & b 
 # adds 2 double bonds(cd,fg), 3 single bonds(bc,df,ga)
 # \   c  
 #  b/   \\d
 # ||      |
 #  a\     f
 # /   g//
               
 connectringat a1 a2 a3 b1 b2 b3 add c d e f               
 
