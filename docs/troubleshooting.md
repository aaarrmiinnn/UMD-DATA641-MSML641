# Troubleshooting Guide

This guide covers common issues you might encounter while setting up and working with the course materials.

---

## 🐍 Python Environment Issues

### Issue: "Python command not found"
**Solution**:
- **Windows**: Add Python to PATH during installation, or use `py` instead of `python`
- **macOS/Linux**: Install Python via homebrew (`brew install python`) or official installer
- **Alternative**: Use Anaconda/Miniconda which handles PATH automatically

### Issue: "pip command not found"
**Solution**:
- Try `python -m pip` instead of `pip`
- On some systems, use `pip3` instead of `pip`
- Reinstall Python with "Add to PATH" option checked

### Issue: Virtual environment not working
**Conda**:
```bash
# Create environment
conda create -n nlp641 python=3.9
conda activate nlp641

# If activation fails
conda init
# Restart terminal, then try again
```

**venv**:
```bash
# Create environment
python -m venv nlp641

# Activate (Windows)
nlp641\\Scripts\\activate

# Activate (macOS/Linux)
source nlp641/bin/activate
```

---

## 📦 Package Installation Issues

### Issue: "Package not found" or installation fails
**Solutions**:
1. **Update pip**: `python -m pip install --upgrade pip`
2. **Use conda-forge**: `conda install -c conda-forge package_name`
3. **Clear cache**: `pip cache purge`
4. **Try different source**: `pip install -i https://pypi.org/simple/ package_name`

### Issue: Version conflicts
**Solutions**:
1. **Create fresh environment**: Start with a new conda/venv environment
2. **Pin versions**: Use exact versions from `requirements.txt`
3. **Use conda**: Often better at resolving dependency conflicts

### Issue: PyTorch installation problems
**CPU only**:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

**CUDA (if you have NVIDIA GPU)**:
```bash
# Check CUDA version first
nvidia-smi
# Then install appropriate version from pytorch.org
```

---

## 🔤 spaCy Issues

### Issue: "Can't find model 'en_core_web_sm'"
**Solution**:
```bash
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_lg

# If download fails, try:
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.4.0/en_core_web_sm-3.4.0.tar.gz
```

### Issue: spaCy model loading errors
**Solutions**:
1. **Check installation**: `python -c "import spacy; print(spacy.info())"`
2. **Reinstall models**: 
   ```bash
   pip uninstall en_core_web_sm
   python -m spacy download en_core_web_sm
   ```
3. **Use alternative loading**:
   ```python
   import spacy.cli
   spacy.cli.download("en_core_web_sm")
   nlp = spacy.load("en_core_web_sm")
   ```

---

## 📚 NLTK Issues

### Issue: "Resource not found" errors
**Solution**:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
```

### Issue: NLTK download fails
**Solutions**:
1. **Manual download location**:
   ```python
   import nltk
   nltk.download('punkt', download_dir='/path/to/nltk_data')
   ```
2. **Alternative download**:
   ```bash
   python -c "import ssl; ssl._create_default_https_context = ssl._create_unverified_context; import nltk; nltk.download('punkt')"
   ```

---

## 🚀 Jupyter Issues

### Issue: Jupyter not starting
**Solutions**:
1. **Try different commands**:
   ```bash
   jupyter notebook
   jupyter lab
   python -m jupyter notebook
   ```
2. **Check port conflicts**: Use `--port=8889` to try different port
3. **Reset config**: `jupyter --config-dir` then delete config files

### Issue: Kernel not found
**Solutions**:
1. **Install kernel in environment**:
   ```bash
   conda activate nlp641
   pip install ipykernel
   python -m ipykernel install --user --name nlp641
   ```
2. **Select correct kernel**: In Jupyter, go to Kernel → Change Kernel

### Issue: Can't import installed packages
**Solution**:
- Make sure Jupyter is running in the same environment where packages are installed
- Check with `!which python` in notebook cell
- Restart kernel after installing packages

---

## 🤗 Transformers Issues

### Issue: Models not downloading
**Solutions**:
1. **Set cache directory**:
   ```python
   import os
   os.environ['TRANSFORMERS_CACHE'] = '/path/to/cache'
   ```
2. **Manual download**:
   ```python
   from transformers import AutoModel, AutoTokenizer
   model_name = "bert-base-uncased"
   tokenizer = AutoTokenizer.from_pretrained(model_name)
   model = AutoModel.from_pretrained(model_name)
   ```
3. **Use offline mode** if you have models cached:
   ```python
   from transformers import pipeline
   classifier = pipeline("sentiment-analysis", local_files_only=True)
   ```

### Issue: CUDA out of memory
**Solutions**:
1. **Reduce batch size**: Use smaller batches for processing
2. **Use CPU**: Add `device=-1` to pipeline
3. **Clear cache**: 
   ```python
   import torch
   torch.cuda.empty_cache()
   ```

---

## 💾 Data and File Issues

### Issue: "File not found" errors
**Solutions**:
1. **Check working directory**: `import os; print(os.getcwd())`
2. **Use absolute paths**: `/full/path/to/file.txt`
3. **Check file permissions**: Make sure files are readable

### Issue: Encoding errors when reading files
**Solution**:
```python
# Try different encodings
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Or handle errors
with open('file.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
```

### Issue: Large dataset loading problems
**Solutions**:
1. **Use chunking**:
   ```python
   import pandas as pd
   for chunk in pd.read_csv('large_file.csv', chunksize=1000):
       process(chunk)
   ```
2. **Use lazy loading**: Load data as needed, not all at once

---

## 🌐 Network and Download Issues

### Issue: Package downloads timeout
**Solutions**:
1. **Increase timeout**: `pip install --timeout 1000 package_name`
2. **Use different index**: `pip install -i https://pypi.org/simple/ package_name`
3. **Download manually**: Download wheel files and install locally

### Issue: Firewall/proxy problems
**Solutions**:
1. **Configure pip for proxy**:
   ```bash
   pip install --proxy http://proxy.server:port package_name
   ```
2. **Set environment variables**:
   ```bash
   export HTTP_PROXY=http://proxy.server:port
   export HTTPS_PROXY=http://proxy.server:port
   ```

---

## 🖥️ Platform-Specific Issues

### Windows Issues
- **Long path problems**: Enable long paths in Windows settings
- **PowerShell execution policy**: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- **Antivirus interference**: Add Python and conda folders to exclusions

### macOS Issues
- **Command line tools**: `xcode-select --install`
- **Homebrew conflicts**: Use virtual environments to isolate packages
- **Permission denied**: Use `sudo` sparingly, prefer user installations

### Linux Issues
- **Missing system libraries**: Install build tools (`build-essential`, `python3-dev`)
- **Permission issues**: Don't use `sudo pip`, use `--user` flag instead
- **Distribution conflicts**: Use conda or virtual environments

---

## 🔍 Debugging Strategies

### General Debugging Steps
1. **Read the error message** carefully - it often tells you exactly what's wrong
2. **Check your environment** - are you in the right conda/venv?
3. **Restart everything** - kernel, terminal, Jupyter, etc.
4. **Start simple** - test with minimal examples first
5. **Search online** - copy/paste error messages into Google

### Getting Detailed Error Information
```python
import traceback
try:
    # your code here
    pass
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
```

### Environment Debugging
```python
import sys
print("Python executable:", sys.executable)
print("Python path:", sys.path)
print("Installed packages:")
import pkg_resources
for pkg in pkg_resources.working_set:
    print(f"  {pkg.key}: {pkg.version}")
```

---

## 📞 Getting Help

### Self-Help Resources
1. **Documentation**: Always check official docs first
2. **Stack Overflow**: Search for your specific error message
3. **GitHub Issues**: Check the issues page for relevant libraries
4. **Course Materials**: Review setup instructions and examples

### Course Resources
1. **Discussion Forum**: Post questions for peer help
2. **Office Hours**: 
   - Instructor: By appointment
   - TAs: See syllabus for schedules
3. **Email**: For urgent issues only

### When Asking for Help
Include:
1. **Error message**: Full traceback, not just "it doesn't work"
2. **Environment info**: OS, Python version, package versions
3. **Code snippet**: Minimal example that reproduces the problem
4. **What you tried**: Show that you've attempted to solve it

---

## ⚡ Performance Tips

### Speed up package installation
```bash
# Use conda-forge channel
conda config --add channels conda-forge

# Parallel downloads
pip install --upgrade pip setuptools wheel
pip install package_name --use-feature=fast-deps

# Use mamba (faster conda)
conda install mamba -n base -c conda-forge
mamba install package_name
```

### Jupyter performance
- Close unused notebooks
- Restart kernel periodically  
- Use `%time` and `%timeit` to profile code
- Consider JupyterLab for better performance

### Memory management
```python
import gc
# Force garbage collection
gc.collect()

# Monitor memory usage
import psutil
print(f"Memory usage: {psutil.virtual_memory().percent}%")
```

---

**Remember**: Most issues have been encountered by others before. Don't hesitate to search online or ask for help!