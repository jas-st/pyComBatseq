# pyreComBat-seq - WIP

It should follow the same logic as reComBat-seq (R version), but is work in progress until the iterations for complex conditions don't take hours to finish.


What I changed so far - added regularization penalties to the objective function in the `glm_levenbeg.py` function.
```python
# lambda_reg - regularisation strength
# alpha - controls (ridge/lasso); 0 - ridge, 1 - lasso
ridge_penalty = lambda_reg * (1 - alpha_reg)
xtwx[:, np.arange(design.shape[1]), np.arange(design.shape[1])] += ridge_penalty

dl = deriv @ design
# REGULARIZATION 
dl -= lambda_reg * (alpha_reg * np.sign(beta) + (1 - alpha_reg) * beta)
```

# Arguments

  - `counts` - raw count matrix from genomic studies (dimensions gene x sample)
  - `batch` - batch covariate (only one vector allowed)
  - `group` - vector / factor for condition of interest
  - `covar_mod` - model matrix for other covariates to include in linear model besides batch and condition of interest

The regularization parameters added are the following:

  - `lambda_reg` - controls the strength of the regularization, $\lambda$ in the above equation
  - `alpha_reg` - controls the elastic net tuning, $\alpha$ in the above equation

# Use Case

```python
adjusted_reg = pcb.pycombat_seq(counts=counts, batch=batches, covar_mod=covmat, alpha_reg=0.3, lambda_reg=0.8)
```
