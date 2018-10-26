function turn(color, matrix, strength, x, y){
	if(strength < 5){
		return heal();
	}
	var randint = Math.floor(Math.random() * 7); 
	var part = Math.floor(strength/2)
	if(randint == 1){
		return move("U", part);
	}
	if(randint == 2){
		return move("D", part);
	}
	if(randint == 3){
		return move("L", part);
	}
	if(randint == 4){
		return move("R", part);
	}
		return heal();
}