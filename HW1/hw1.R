# CS676 Algorithms - HW1

X <- c(3, 1, 2, 3, 1, 4, 3, 3)
Y <- c(1, 4, 3, 1, 1, 3)
Z <- c(3, 3, 1, 4, 2, 1, 4, 2)

sumall <- function(X) {
  s <- 0
  for (x in X) {
    s <- s + x
  }
  return(s)
}

sumall(X)
sumall(Y)
sumall(Z)

## Median
mymedian <- function(X) {
  S = sort(X)
  n <- length(S)
  return((S[floor((n+1)/2)] + S[ceiling((n+1)/2)])/2)
}

mymedian(X)
mymedian(Y)
mymedian(Z)

## Arithmetic Mean
amean <- function(X) {
  s <- 0
  for (x in X) {
    s <- s + x
  }
  return(s/length(X))
}

amean(X)
amean(Y)
amean(Z)

## Geometric Mean
gmean <- function(X) {
  p = 1
  for (x in X) {
    p = p * x
  }
  return(p^(1/length(X)))
}

gmean(X)
gmean(Y)
gmean(Z)

## Harmonic Mean
hmean <- function(X) {
  s = 0
  for (x in X) {
    s = s + 1/x
  }
  return(length(X)/s)
}

hmean(X)
hmean(Y)
hmean(Z)

## Arithmetic-Geometric Mean
agmean <- function(X) {
  am <- amean(X)
  gm <- gmean(X)
  while (abs(am-gm) > 0.000001){
    tmp <- (am + gm)/2
    gm <- (am * gm)^(1/2)
    am <- tmp
  }
  return((am + gm)/2)
}

agmean(X)
agmean(Y)
agmean(Z)

## Arithmetic-Geometric-Harmonic Mean
aghmean <- function(X) {
  am <- amean(X)
  gm <- gmean(X)
  hm <- hmean(X)
  while (abs(am-gm) > 0.000001 | abs(am-hm) > 0.000001| abs(gm-hm) > 0.000001){
    tmpa <- amean(c(am, gm, hm))
    tmpg <- gmean(c(am, gm, hm))
    hm <- hmean(c(am, gm, hm))
    am = tmpa
    gm = tmpg
  }
  return((am + gm + hm)/3)
}

aghmean(X)
aghmean(Y)
aghmean(Z)


# Linear Recursion
ameanR <- function(X) {
  n <- length(X)
  if (n == 1)
    return(X[1])
  else {
    return(((n-1)* ameanR(X[-n]) + X[n])/n)
  }
}

ameanR(X)
ameanR(Y)
ameanR(Z)