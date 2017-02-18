#https://www.codewars.com/kata/563b662a59afc2b5120000c6
def nb_year(p0, percent, aug, p):
    total_live = p0 + p0*percent/100 + aug
    year = 1
    while total_live < p:
        total_live = total_live + total_live*percent/100 + aug
        year = year + 1
    return year
