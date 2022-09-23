import os
import mne
import json
# Load brainlife config.json
with open('config.json','r') as config_f:
    config = json.load(config_f)

# == LOAD DATA ==
fname = config['fif']
raw = mne.io.read_raw_fif(fname, verbose=False)

ica= mne.preprocessing.ICA(n_components=config['n_components'], noise_cov=None,
                      random_state=None, method=config['method'],
                      fit_params=None, max_iter=config['max_iter'],
                      allow_ref_meg=config['allow_ref_meg'])

ica.fit(raw)

ica.save('out_dir/ica.fif')