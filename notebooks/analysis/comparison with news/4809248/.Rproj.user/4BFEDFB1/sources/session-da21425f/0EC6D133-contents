require(trend)

xenophobia_results_total <- read_excel("xenophobia_results_total.xlsx", sheet = "counts - month")

xenophobia_results_total$date_n = 1:nrow(xenophobia_results_total)



ts_xen = ts(xenophobia_results_total$HS)
plot(ts_xen, xlab="Month", ylab="HS tweets")

s.res <- pettitt.test(ts_xen)
n <- s.res$nobs
i <- s.res$estimate
s.1 <- mean(ts_xen[1:i])
s.2 <- mean(ts_xen[(i+1):n])
s <- ts(c(rep(s.1,i), rep(s.2,(n-i))))
tsp(s) <- tsp(ts_xen)
lines(s, lty=2)
title(main = paste0("Frequency of Hate Speech Tweets\n",
                    "Change-Point Detection on month: ",xenophobia_results_total$date[i]))


