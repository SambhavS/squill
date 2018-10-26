function turn(color, matrix, strength, x, y){
	if(strength < 5){
		return heal();
	}
	if(matrix[x+1][y][0] == "red"){
		return attack("R", strength-3);
	}
	if(matrix[x-1][y][0] == "red"){
		return attack("L", strength-3);
	}
	if(matrix[x][y+1][0] == "red"){
		return attack("D", strength-3);
	}
	if(matrix[x][y-1][0] == "red"){
		return attack("U", strength-3);
	}
	var randint = Math.floor(Math.random() * 5); 
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