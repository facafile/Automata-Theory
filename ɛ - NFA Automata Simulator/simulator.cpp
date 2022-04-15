#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//sortiraj vektor i izbaci duplikate iz njega
void dodaj_bez_dupl(vector<string> &vec){
   sort( vec.begin(), vec.end() );
vec.erase( unique( vec.begin(), vec.end() ), vec.end() );
}

//popuni vektor prijelaza sa # na svim mjestima
vector<vector<vector<string>>> popuni_glavni_vektor(int abeceda_size, int stanja_size){
    vector<string> unutarnji;
    vector<vector<string>> srednji;
    vector<vector<vector<string>>> vanjski;
    vector<string> prazan;

    unutarnji.push_back("#");

    for(int i =1; i<=abeceda_size;i++){
        srednji.push_back(unutarnji);
    }
    

    for(int i = 0;i<=stanja_size;i++){
        vanjski.push_back(srednji);
    }

    return vanjski;

}

//od stringa splitanog po zarezima napravi vektor
vector<string> str_u_vec(string input){
    int len=input.length();
    vector<string> output;
    string pom="";
    for(int i =0; i < len; i++){
        if(input[i]==','){
            output.push_back(pom);
            pom="";
        }
        else{
            pom+=input[i];
        }
    }

    output.push_back(pom);

    return output;
}

//od prvog reda inouta napravi tablicu sa ulaznim nizovima
vector<vector<string>> punjenje_tab(string ulaz){

    vector<vector<string>> pom1;
    int len=ulaz.length();
    string pom="";

    for(int i =0; i < len; i++){
        if(ulaz[i]=='|'){
            pom1.push_back(str_u_vec(pom));
            pom="";
        }
        else{
            pom+=ulaz[i];
        }
    }

    pom1.push_back(str_u_vec(pom));
    return pom1;

}

//napravi string od elemenata vektora odvojenih zarezom
string ispisi_1d(vector<string> vektor){
    string str="";
    for(long unsigned int i=0;i<vektor.size();i++){
        str+=vektor[i]+",";
    }
    return str;
}

//ovo je samo za moj feedback da vidim jel mi dobro popunilo tablicu prijelaza
void ispisi_3d(vector<vector<vector<string>>> vektor){
    for(long unsigned int i =0;i<vektor.size();i++){
        for(long unsigned int j=0;j<vektor[i].size();j++){
            for(long unsigned int k=0;k<vektor[i][j].size();k++){
                cout<<vektor[i][j][k]<<",";
            }
            cout<<"  ";
        }
        cout<<"\n";
    }
}

//uzmi vektor i u njemu pronadi index trazenog elementa
long unsigned int find_index(vector<string> vektor,string slovo){

    if(slovo=="#")return vektor.size();
    
    for(long unsigned int i=0;i<vektor.size();i++){
        if(slovo==vektor[i])return i;
    }
    return -1;
}

//odredi u kojima smo jos stanjima ovisno jesu li trenutna povezana s jos nekima s epsilon izrazima
void epsilon_pr(vector<string> &vektor,vector<vector<vector<string>>> tablica,vector<string> stanja){
    int x=vektor.size();
    vector<string> pom;
    for(int i =0;i<x;i++){
        pom=tablica[find_index(stanja,vektor[i])][0];
        for(auto el : pom){
            if(find(vektor.begin(),vektor.end(),el)==vektor.end() && el!="#"){
                vektor.push_back(el);
                x++;
            }
        }
    }
    dodaj_bez_dupl(vektor);
}

//GLAVNI PROGRAM
int main(void){
    string red;
    vector<vector<string>> data_tablica;
    vector<vector<vector<string>>> tablica_razvoja;
    vector<string> stanja;
    vector<string> prih_stanja;
    vector<string> abeceda;
    string poc_stanje;
    vector<string> funkcija_a;

    //1. red
    cin>> red;
    data_tablica=punjenje_tab(red);

    //2.red
    cin>> red;
    stanja=str_u_vec(red);

    //3.red
    cin>> red;
    funkcija_a=str_u_vec(red);
    abeceda.push_back("$");
    for(long unsigned int x=0; x<funkcija_a.size();x++)abeceda.push_back(funkcija_a[x]);

    //4.red
    cin>> red;
    prih_stanja=str_u_vec(red);

    //5.red
    cin>> poc_stanje;

    //6. i daljnji redovi
    string str1;
    string str2;
    
    int del;
    tablica_razvoja=popuni_glavni_vektor(abeceda.size(),stanja.size());
    
    
    while(cin>>red){
        del = red.find("->");
        str1=red.substr(0,del);
        str2=red.substr(del+2);
        //cout<<str1<<"     "<<str2<<"\n";
        funkcija_a=str_u_vec(str1);
        //cout<<find_index(stanja,funkcija_a[0])<<" -> "<<find_index(abeceda,funkcija_a[1])<<"\n";
        tablica_razvoja[find_index(stanja,funkcija_a[0])][find_index(abeceda,funkcija_a[1])]=str_u_vec(str2);
        

    }
    //ispisi_3d(tablica_razvoja);

    //simulacija automata
    int test;
    for(auto niz : data_tablica){

        vector<string> tren_stanja;
        vector<string> slj_stanje;
        vector<string> pom1;
        vector<string> prazan;
        string ispis;

        tren_stanja.push_back(poc_stanje);
        epsilon_pr(tren_stanja,tablica_razvoja,stanja);
        
        //pom1=tablica_razvoja[find_index(stanja,poc_stanje)][0];
        //if(pom1[0]!="#")tren_stanja.insert(tren_stanja.end(),pom1.begin(),pom1.end());

        ispis=ispisi_1d(tren_stanja);
        ispis.resize(ispis.size()-1);
        cout<<ispis;

        for(auto znak : niz){
            test=0;
            cout<<"|";

            for(auto stanje: tren_stanja){
                pom1=tablica_razvoja[find_index(stanja,stanje)][find_index(abeceda,znak)];

                if(pom1[0]!="#"){
                    slj_stanje.insert(slj_stanje.end(),pom1.begin(),pom1.end());
                    test=1;
                }
            }

            if(test==0)slj_stanje.push_back("#");
            dodaj_bez_dupl(slj_stanje);
            tren_stanja=slj_stanje;
            slj_stanje=prazan;
            epsilon_pr(tren_stanja,tablica_razvoja,stanja);

            ispis=ispisi_1d(tren_stanja);
            ispis.resize(ispis.size()-1);
            cout<<ispis;

        }
        tren_stanja=prazan;
        cout<<"\n";
    }


    return 0;
}