from datetime import timedelta
from enum import Enum


class TipoAbono(Enum):
    MENSUAL = ("Mensual", 25.00, timedelta(days=30))
    TRIMESTRAL = ("Trimestral", 70.00, timedelta(days=91))
    SEMESTRAL = ("Semestral", 130.00, timedelta(days=182))
    ANUAL = ("Anual", 200.00, timedelta(days=365))
