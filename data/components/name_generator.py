from random import choice

names = """James Linda Robert Mary John Patricia Michael Barbara David Susan
                  William Nancy Richard Deborah Thomas Sandra Charles Carol Gary
                  Kathleen Larry Sharon Ronald Karen Joseph Donna Donald Brenda 
                  Kenneth Margaret Steven Diane Dennis Pamela Paul Janet Stephen 
                  Shirley George Carolyn Daniel Judith Edward Janice Mark Cynthia 
                  Jerry Elizabeth Gregory Judy Bruce Betty Roger Joyce Douglas 
                  Christine Frank Cheryl Terry Gloria Raymond Beverly Timothy Martha 
                  Lawrence Bonnie Gerald Catherine Wayne Dorothy Anthony Rebecca 
                  Peter Marilyn Patrick Kathy Danny Jane Walter Joan Alan Peggy Willie 
                  Gail Jeffrey Virginia Carl Connie Harold Ann Arthur Kathryn Henry 
                  Diana Jack Jean Dale Ruth Johnny Helen Roy Frances Ralph Wanda 
                  Philip Phyllis Joe Paula Jimmy Jacqueline Albert Rita Billy Alice 
                  Eugene Katherine Glenn Debra Stanley Elaine Harry Vicki Samuel 
                  Sherry Howard Laura Phillip Jo Bobby Theresa Louis Ellen Russell 
                  Joanne Andrew Marsha Craig Rose Randall Sheila Allen Suzanne 
                  Christopher Marie Kevin Maria Barry Doris Frederick Cathy Ronnie 
                  Lynn Leonard Marcia Keith Sally Brian Darlene Randy Charlotte Ernest
                  Teresa Scott Denise Fred Lois Steve Anne Martin Constance Francis 
                  Evelyn Melvin Glenda Rodney Sarah Eddie Maureen Norman Dianne 
                  Lee Eileen Earl Irene Marvin Anna Tommy Victoria Clarence Jeanne 
                  Alfred Roberta Curtis Sylvia Eric Joann Theodore Anita Clifford Sue
             """
lasts = """SMITH JOHNSON WILLIAMS JONES BROWN DAVIS MILLER WILSON
               MOORE TAYLOR ANDERSON THOMAS JACKSON WHITE HARRIS 
               MARTIN THOMPSON GARCIA MARTINEZ ROBINSON CLARK 
               RODRIGUEZ LEWIS LEE WALKER HALL ALLEN YOUNG HERNANDEZ 
               KING WRIGHT LOPEZ HILL SCOTT GREEN ADAMS BAKER GONZALEZ 
               NELSON CARTER MITCHELL PEREZ ROBERTS TURNER PHILLIPS 
               CAMPBELL PARKER EVANS EDWARDS COLLINS STEWART SANCHEZ 
               MORRIS ROGERS REED COOK MORGAN BELL MURPHY BAILEY RIVERA
               COOPER RICHARDSON COX HOWARD WARD TORRES PETERSON 
               GRAY RAMIREZ JAMES WATSON BROOKS KELLY SANDERS PRICE 
               BENNETT WOOD BARNES ROSS HENDERSON COLEMAN JENKINS 
               PERRY POWELL LONG PATTERSON HUGHES FLORES WASHINGTON 
               BUTLER SIMMONS FOSTER GONZALES BRYANT ALEXANDER RUSSELL
               GRIFFIN DIAZ HAYES MYERS FORD HAMILTON GRAHAM SULLIVAN 
               WALLACE WOODS COLE WEST JORDAN OWENS REYNOLDS FISHER 
               ELLIS HARRISON GIBSON MCDONALD CRUZ MARSHALL ORTIZ 
               GOMEZ MURRAY FREEMAN WELLS WEBB SIMPSON STEVENS TUCKER
               PORTER HUNTER HICKS CRAWFORD HENRY BOYD MASON MORALES 
               KENNEDY WARREN DIXON RAMOS REYES BURNS GORDON SHAW 
               HOLMES RICE ROBERTSON HUNT BLACK DANIELS PALMER MILLS 
               NICHOLS GRANT KNIGHT FERGUSON ROSE STONE HAWKINS DUNN 
               PERKINS HUDSON SPENCER GARDNER STEPHENS PAYNE PIERCE 
               BERRY MATTHEWS ARNOLD WAGNER WILLIS RAY WATKINS OLSON 
               CARROLL DUNCAN SNYDER HART CUNNINGHAM BRADLEY LANE 
               ANDREWS RUIZ HARPER FOX RILEY ARMSTRONG CARPENTER 
               WEAVER GREENE LAWRENCE ELLIOTT CHAVEZ SIMS AUSTIN 
               PETERS KELLEY FRANKLIN LAWSON
           """               

FIRST_NAMES = names.split()
LAST_NAMES = [x.title() for x in lasts.split()]


def generate_name():
    return "{} {}".format(choice(FIRST_NAMES), choice(LAST_NAMES))