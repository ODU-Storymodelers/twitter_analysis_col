library(mcp)
library(readxl)
library(patchwork)
library(EnvCpt)
library(loo)
library(ggplot2)
set.seed(1234)
frustration_col <- read_excel("negative_tweets+news_comparison.xlsx", sheet = "Greece-original-ts")
frustration_col$date_n = 1:nrow(frustration_col)

subjs <- colnames(frustration_col)#[2:6]
fit2cp = mcp(model2cp, data = frustration_col, par_x = "date_n",)

for (subj in subjs[-1]){
  model2cp = list(Y~1, 1~1, 1~1)  
  frustration_col['Y'] = frustration_col[subj]
  fit2cp = mcp(model2cp, data = frustration_col, par_x = "date_n",)
  
  
  #model0cp = list(Y~1) 
  #model1cp = list(Y~1, 1~1)
  #fit0cp = mcp(model0cp, data = frustration_col, par_x = "date_n")
  #fit1cp = mcp(model1cp, data = frustration_col, par_x = "date_n")
  
  m = summary(fit2cp)
  parms = round(m$mean,1)
  month1 = frustration_col$date[parms[1]]
  month2 = frustration_col$date[parms[2]]
  
  x = plot(fit2cp)+ 
    theme_light()+ 
    geom_line()+
    labs(title = paste("Change point for Greece",subj),
         subtitle = paste("Change points detected in",month1, "and",month2),
         caption = "",
         x = "Month",
         y = "Frustration codes",
    )
  
  ggsave(paste0("./plots/",subj,".png"), x, width = 8, height = 5)
}

subj <- subjs[4]
model2cp = list(Y~1, 1~1, 1~1)  
frustration_col['Y'] = frustration_col[subj]
fit2cp = mcp(model2cp, data = frustration_col, par_x = "date_n")
m = summary(fit2cp)
parms = round(m$mean,1)
month1 = frustration_col$date[parms[1]]
month2 = frustration_col$date[parms[2]]

x = plot(fit2cp)+ 
  theme_light()+ 
  geom_line()+
  labs(title = paste("Change point for Greece",subj),
    subtitle = paste("Change points detected in",month1, "and",month2),
    caption = "",
    x = "Month",
    y = "Frustration codes",
  )

ggsave('plot.png', x, width = 8, height = 5)
