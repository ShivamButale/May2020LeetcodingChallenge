int numJewelsInStones(char * J, char * S){

    int i, j, jwl = 0;
    for(i = 0; i < strlen(J); i++){
        //printf("%c",J[i]);
        for(j = 0; j < strlen(S); j++){
            if(S[j] == J[i])
                jwl++;
        }
    }
    return jwl;
}
