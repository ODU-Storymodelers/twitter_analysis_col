library(mcp)
library(readxl)
library(patchwork)
library(EnvCpt)
library(loo)

set.seed(1234)


cp_n_list(0)
xenophobia_results_total <- read_excel("xenophobia_results_total.xlsx", sheet = "counts - month")

xenophobia_results_total$date_n = 1:nrow(xenophobia_results_total)


cp_n_list <- function(n=0) { # create a function with the name my_function
  m = list(colnames(xenophobia_results_total)[1]~1)
  if (n>0){
    for (i in 2:(n+1)){
      m[[i]]=1~1
    }
  }
  
  return(m)
}



# 0 changepoint
fit_mcp_col1 = mcp(cp_n_list(0), data = xenophobia_results_total, par_x = "date_n")

plot(fit_mcp_col1, geom_data = "line") + ggtitle("Change-Point Detection on month:") + theme_bw(15)
fit_mcp_col1

model2 = list(Y~1, 1~1)  # 1 changepoint
fit_mcp_col2 = mcp(cp_n_list(1), data = xenophobia_results_total, par_x = "date_n", par_y = "")

m = summary(fit_mcp_col2)
m$mean[1]  
month = xenophobia_results_total$date[m$mean[1]]
plot(fit_mcp_col2, geom_data = "line", lines =20) + 
  theme_bw(15) + 
  labs(title=paste0("Change-Point Detection on month: ", month),
        x ="Month", y = "Frustration count")

model3 = list(Y~1, 1~1, 1~1)  # 2 changepoint
xenophobia_results_total['Y'] = xenophobia_results_total['HS']
fit_mcp_col3 = mcp(model3, data = xenophobia_results_total, par_x = "date_n")
plot(fit_mcp_col3)

loo::loo_compare(loo(fit_mcp_col1),loo(fit_mcp_col2),loo(fit_mcp_col3))


fit_mcp_col2

xenophobia_results_total$date[70]

fit_mcp_col3
xenophobia_results_total$date[57]
xenophobia_results_total$date[71]


frustration_col <- read_excel("negative_tweets+news_comparison.xlsx", sheet = "Greece-original-ts")
frustration_col$date_n = 1:nrow(frustration_col)

subjs <- colnames(frustration_col)#[2:6]

subj = subjs[17]
model2cp = list(Y~1, 1~1, 1~1)  
frustration_col['Y'] = frustration_col[subj]
fit2cp = mcp(model2cp, data = frustration_col, par_x = "date_n")
m = summary(fit2cp)
month1 = xenophobia_results_total$date[m$mean[1]]
month2 = xenophobia_results_total$date[m$mean[2]]

plot(fit2cp, geom_data = "line", lines =20,q_fit = TRUE) + 
  theme_bw(15) + 
  labs(title=paste(sep = " ","Change-Point Detection on months:", month1,',',
                   month2,"\nGreece - ",subj),
       x ="Month", y = "Frustration count")

model0cp = list(Y~1) 
model1cp = list(Y~1, 1~1)
fit0cp = mcp(model0cp, data = frustration_col, par_x = "date_n")
fit1cp = mcp(model1cp, data = frustration_col, par_x = "date_n")
model_names = c("model1"="No Change-point", "model2"="1 Change-point", "model3"="2 Change-points")
comparison = loo_compare(loo(fit0cp),loo(fit1cp),loo(fit2cp))
row_names = list()
for (i in rownames(comparison)){
  row_names <- append(row_names, model_names[i])
}
rownames(comparison)= row_names

print(paste("Comparison for Colombia: 0, 1 and 2 change-points",
            "\nColombia -",subj))
comparison

