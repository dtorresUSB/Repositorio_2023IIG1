#1. Conocer el numero de copas mundo que un país ha ganado
#2. Conocer el numero de subcampeonatos que un país ha ganado
#3. Conocer el numero de participaciones de un equipo al mundial
#4. Conocer el numero de copas mundiales jugadas hasta la fecha
#5. Conocer el número de asistentes a las copas mundiales
#6. Conocer el número de finales disputadas por penales
#7. Conocer el número de goles a favor de los equipos en los mundiales'
#8. Conocer el número de goles en contra de los equipos en los mundiales'
#9. Conocer la diferencia de goles en todas sus presentaciones'
#10. Conocer el promedio de goles de un equipo en mundiales'
#['home_team', 'away_team', 'home_score', 0-2
#'home_penalty', 'away_score', 'away_penalty',3-5
#'home_manager', 'home_captain', 'away_manager', 6-8
#'away_captain', 'Attendance', 'Venue', 'Round', 9-12
# 'Date', 'Referee', 'Host', 'Year'] 13-16

def subcampeon_mundial(listado):
    subcampeones={}
    for partidos in listado:
        if partidos[12]=='Final':
            if (partidos[2]>partidos[4])or(partidos[3]>partidos[5]):
                if partidos[1] not in subcampeones:
                    subcampeones[partidos[1]]=[partidos[16]]
                else:
                    list_year=subcampeones[partidos[1]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[1]]=list_year                
            else:
                if partidos[0] not in subcampeones:
                    subcampeones[partidos[0]]=[partidos[16]]
                else:
                    list_year=subcampeones[partidos[0]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[0]]=list_year
    print(subcampeones)


def campeon_mundial(listado):
    campeones={}
    for partidos in listado:
        if partidos[12]=='Final':
            if (partidos[2]>partidos[4])or(partidos[3]>partidos[5]):
                if partidos[0] not in campeones:
                    campeones[partidos[0]]=[partidos[16]]
                else:
                    list_year=campeones[partidos[0]]
                    list_year.append(partidos[16])
                    campeones[partidos[0]]=list_year                
            else:
                if partidos[1] not in campeones:
                    campeones[partidos[1]]=[partidos[16]]
                else:
                    list_year=campeones[partidos[1]]
                    list_year.append(partidos[16])
                    campeones[partidos[1]]=list_year
    campeones=dict(sorted(campeones.items()))
    print('\n---------------Listado de Campeones mundiales ----------------\n')
    for pais,year in campeones.items():
        print(f'{pais}: campeón en {year}')
    
    pais=input('Ingrese un pais: ')
    
    if pais in campeones:
        year=campeones[pais]
        print(f'fue campeon en los años {year}')
    else:
        print(f'{pais} no ha sido campeon del mundo')