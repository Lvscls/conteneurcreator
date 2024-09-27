import pytest
import subprocess
from conteneurcreator import is_docker_installed

def test_system_detection_linux(monkeypatch):
    # Simuler que le système d'exploitation est Linux
    monkeypatch.setattr('platform.system', lambda: "Linux")
    from platform import system
    assert system() == "Linux"

def test_system_detection_windows(monkeypatch):
    # Simuler que le système d'exploitation est Windows
    monkeypatch.setattr('platform.system', lambda: "Windows")
    from platform import system
    assert system() == "Windows"

def test_system_detection_unknown(monkeypatch):
    # Simuler un système d'exploitation inconnu
    monkeypatch.setattr('platform.system', lambda: "UnknownOS")
    from platform import system
    assert system() == "UnknownOS"

def test_is_docker_installed(monkeypatch):
    # Simuler que Docker est installé (la commande réussit)
    def mock_run(args, **kwargs):
        return subprocess.CompletedProcess(args, 0)  # Retourne un code de sortie 0 (succès)

    monkeypatch.setattr(subprocess, 'run', mock_run)
    assert is_docker_installed() == True

def test_is_docker_not_installed(monkeypatch):
    # Simuler que Docker n'est pas installé (la commande échoue)
    def mock_run_fail(args, **kwargs):
        raise FileNotFoundError()  # Simule l'absence de Docker

    monkeypatch.setattr(subprocess, 'run', mock_run_fail)
    assert is_docker_installed() == False