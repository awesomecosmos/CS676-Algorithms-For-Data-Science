library(ramify)

R <- mat(
"1, 2, 0; 
3, 3, 0; 
5, 4, 0; 
6, 4, 0; 
2, 1, 1; 
7, 2, 1; 
6, 1, 1")

nr <- dim(R)[1]
nc <- dim(R)[2]

d <- nc - 1
q <- mat("3, 1")
r <- R[1, 1:2]

p = 3
(sum((abs(q - r))^p))^(1/p)
L2q = array(0, dim=c(nr,1))
for(i in 1:nr){
  L2q[i] = sqrt(sum((q - R[i,1:d])^2))
}
L2q

NNclassifier <- function(q, R) {
  nr = dim(R)[1]
  nc = dim(R)[2]
  d = nc - 1
  L2q = array(0, dim=c(nr,1))
  for(i in 1:nr){
    L2q[i] = sqrt(sum((q - R[i,1:d])^2))
  }
  return(R[which.min(L2q),nc])
}

kNNclassifier <- function(q, R, k) {
  nr = dim(R)[1]
  nc = dim(R)[2]
  d = nc - 1
  L2q = array(0, dim=c(nr,1))
  for(i in 1:nr){
    L2q[i] = sqrt(sum((q - R[i,1:d])^2))
  }
  T = order(L2q)
  V = array(0, dim=c(1,max(R[,nc])))
  for(i in 1:k){
    V[R[T[i],nc]] = V[R[T[i],nc]] + 1
  }
  return(which.max(V))
}