# anti-cheat 
import sys
sys.exit = exit = None

from re import fullmatch

# verify user solution
def verify(r,sol,ref):
	if ref == None:
		if sol == None: return (True,)
		else: return (False,'This puzzle has no solution')
	if type(sol) != list:
		return (False,'Data type must be a list')
	if not all(type(s) == str and fullmatch(r'[NWSE]*',s) for s in sol):
		return (False,'All list elements must be a string and may only contain the following characters: "NWSE"')
	
	def celrot(n): return sum(divmod(n<<1,16))
	def cel_layout(n): return tuple(n%(x<<1)//x for x in (8,4,2,1))
	
	ref_str = 'Here is a valid solution:\n[{}]'.format(', '.join(f"'{s}'" for s in ref))
	user_str = 'Here is your solution:\n[{}]'.format(', '.join(f"'{s}'" for s in sol))
	
	if len(sol) > len(ref):
		return (False,f'Your solution completes the task in {len(sol)} iterations.\nThis test can be completed in {len(ref)} iterations.\n' + ref_str + '\n' + user_str)
	
	walls_list = tuple(cel_layout(n) for n in range(16))
	dnum = {'N':0, 'W':1, 'S':2, 'E':3}
	dirs = {'N':(-1,0), 'W':(0,-1), 'S':(1,0), 'E':(0,1)}
	dwrd = ['north','west','south','east']
	phase = tuple(tuple(x if type(x) == int else 0 for x in row) for row in r)
	phases = [phase]
	for _ in range(3):
		phase = tuple(tuple(celrot(x) for x in row) for row in phase)
		phases.append(phase)
	
	xl,yl = len(r),len(r[0])
	for i,row in enumerate(r):
		for j,cel in enumerate(row):
			if type(cel) == str:
				if cel == 'B': pos = (i,j)
				else: dst = (i,j)
	
	px,py = pos
	bad_move = lambda s: (False,f'Invalid move: {s}\n{user_str}')
	for i,s in enumerate(sol):
		cr = phases[i%4]
		visited = set()
		for j,ss in enumerate(s):
			nx,ny = dirs[ss]
			px,py = (nx+pos[0],ny+pos[1])
			pos_str = 'during move {} at iteration {}.\nLast valid position was [{}, {}].'.format(j,i,*pos)
			if px < 0 or px >= xl or py < 0 or py >= yl:
				return bad_move(f'Out of bounds {pos_str}')
			
			# check for walls obstructing path
			wall0 = walls_list[cr[pos[0]][pos[1]]][dnum[ss]]
			wall1 = walls_list[cr[px][py]][(dnum[ss]+2)%4]
			obstruct = 1 if wall0 else 2 if wall1 else 0
			if obstruct:
				return bad_move(f'Path obstructed by a wall on the {dwrd[[dnum[ss],(dnum[ss]+2)%4][obstruct-1]]} side of {[f"[{pos[0]}, {pos[1]}]",f"[{px}, {py}]"][obstruct-1]} {pos_str}')
			if (px,py) in visited:
				return bad_move(f'Entered cell [{px},{py}] a second time {pos_str}')
			pos = (px,py)
			visited.add(pos)
	
	if pos != dst:
		last_pos = f' Its last position was [{px},{py}]' if px != None and py != None else ''
		return (False,f'The ball did not reach the destination.{last_pos}\n{user_str}')
	
	return (True,'')