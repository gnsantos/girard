from matplotlib import pyplot as plt

def plot_multiple_functions(xrange, fn, parameters, title, xlabel, ylabel, legend_title):
    plt.yscale("log")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for p in parameters:
        plt.plot(xrange, fn(p, xrange), label=str(p))
    plt.legend(loc="upper right", title=legend_title)
    plt.show()


def plt_dim(d, b=50):
    eight = df_its[df_its["dimension"] == d]
    eight = eight["its_to_convergs"]
    m = max(eight)
    xt = 10*(m // b)
    plt.hist(eight, bins=b, density=False)
    plt.xticks(range(1, m, xt))
    plt.show()


def plot_distribution(estimators, mean, n_bins=25):
    ax = sns.distplot(estimators, fit=scipy.stats.norm, bins=n_bins, kde=False, hist=True, color='g', norm_hist=True)
    ax.set_title("Distribution for solid angle estimator")
    plt.legend(["Sample distributed", "Predicted Distribution"])
    plt.axvline(mean, 120)
    plt.show()


def build_and_plot_distribution(cone_vectors, samples_per_estimate, population_size, n_bins=25):
    estimators, mean, rstd, pstd = get_sample_distribution_for_solid_angle(cone_vectors, samples_per_estimate, population_size)
    plot_distribution(estimators, n_bins)
    return  estimators, mean, rstd, pstd


def create_plot(estimators, real_value, breaks=13, n_bins=21):
    mean = np.mean(estimators)
    std = np.std(estimators)
    ax = sns.distplot(estimators, fit=scipy.stats.norm, bins=n_bins, kde=False, hist=True, color='#e3ace3', norm_hist=True)
    ax.axvline(mean, color='#c46745', drawstyle='steps-mid', linestyle='--')
    ax.axvline(real_value, color='#69bcc2', drawstyle='steps-mid', linestyle='--')
    plt.title("Distribution of estimators for $\omega_K$")
    ax.legend(['Fitted Distribution', 'Mean', 'Acutal Solid Angle', 'Sampled Distribution'])
    plt.xlabel("Estimate of $\omega_K$")
    plt.ylabel("Estimate frequency")
    plt.xticks(np.linspace(mean - 3*std, mean + 3*std, breaks))
    plt.show()


def plot_experiments(df, dimensions):
    plt.xticks(dimensions)
    plt.xlabel("Dimension")
    plt.yscale("log")
    plt.ylabel("Samples Until Finding A Cone in Region of Convergence")
    sns.lineplot(data=df, markers=True,)
    plt.show()
