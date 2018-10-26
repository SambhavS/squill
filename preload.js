//Utils
function max(n1, n2){
	if(n1>n2){
		return n1;
	}
	return n2;
}
//Moves
function move(dir, num) {
	return["move", dir, max(0, num)]
}
function heal(){
	return ["heal"];
}
function attack(dir, num){
	return ["attack", dir, max(0, num)]
}