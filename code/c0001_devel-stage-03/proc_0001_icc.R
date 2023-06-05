knitr::opts_chunk$set(echo = TRUE)
library(tidyverse)
library(moments)
library(tm)#Function to remove strings
library(reshape2)#for data manipulation
library(nlme)#for ICC
library(multilevel)#for ICC
library(arsenal)#for dataframe comparisons
library(jtools)#for theme_apa function for plots
library(apaTables)#for APA format tables
library(fuzzyjoin)

# SWITCH DATA
dir0 <- "../../data/d0008_synsets-evaluated/"
if0 <- "long.csv"

ratings_icc <- read_csv(file = file.path(dir0, if0))
spec(ratings_icc)
ratings_icc

#Calculate ICC based on function from psychometric package but customized optimizer (see Brysbaert et al. 2019 for method description)
#Run multilevel model with optimizer set to optim
attach(ratings_icc)
mod <- lme(EVAL ~ 1, random = ~1 | OEWN, na.action = na.omit, control = lmeControl(opt = "optim"))
detach(ratings_icc)
#Extract intercept variance
t0 <- as.numeric(VarCorr(mod)[1,1])
#Extract residual variance
sig2 <- as.numeric(VarCorr(mod)[2,1])
#Calculate ICC based on intercept and residual variance
icc1 <- t0/(t0 + sig2)
#Calculate mean ICC across all group ICCs
# icc2 <- mean(GmeanRel(mod)$MeanRel)
icc2 <- mean(gmeanrel(mod)$MeanRel)
paste(icc1)
paste(icc2)
