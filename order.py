# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 09:51:53 2020

@author: Ramarao Chowdary B
"""
name=input("Please, Enter your name:\n")
print("Welcome,Mr/Mrs."+str(name)+". you are in HUNGREE.")
print("Here is your Menu:")
print("-------------------------------------------------------------------")
print("STARTERS        |  SOUPS                | MEALS                   |")
print("----------------|-----------------------|-------------------------|")
print("FRIED CHICKEN   |CORN SOUP              | MEMONI BIRYAANI         |")
print("CHICKEN TIKKA   |TOMATO SOUP            | HYDERABADI BIRYAANI     |")
print("CHICKEN KEEMA   |ONION SOUP             | MOGALAYI BIRYAANI       |")
print("PANEER 65       |MUSHROOM SOUP          | VEG DHUM BIRYAANI       |")
print("VEG KABAB       |CHICKEN SWEET CORN SOUP| PRAWNS BIRYAANI         |")
print("BREAD ROLL      |CHICKEN MANCHOW SOUP   | MALBAR BIRYAANI         |")
print("PANNER MANCHRIAN|SEA FOOD SOUP          | MUTTON BIRYAANI         |")
print("VEG SPRING ROOLL|CHICKEN SHORBA SOUP    | FISH BIRYAANI           |")
print("VEG CUTLET      |THAI PRAWNS SOUP       | KEEMA BIRYAANI          |")
print("GOBI MANCHURIAN |CRAB MEAT SOUP         | ALOO DHUM BIRYAANI      |")
print("!_!_!_!_!_!_!_!_!_!_!_!_!_!_!ORDER PLS_!_!_!_!_!__!_!_!_!_!_!_!_!_!")
isel=input("Do you want any STARTERS or SOUPS or MEALS")
if str(isel)=="STARTERS" or str(isel)=="Starters" or str(isel)=="starters":
    storder=input("Pls mention your item/s seperated by comma(,):\n")
    sop=input("Do you want any SOUPS:(type YES/NO)")
    if str(sop)=="yes" or str(isel)=="YES" or str(isel)=="Yes":
        sorder=input("Pls mention your item/s seperated by comma(,):")
        mop=input("Do you want any MEALS:(type YES/NO)")
        if str(mop)=="yes" or str(mop)=="YES" or str(mop)=="Yes":
            morder=input("Pls mention your item/s seperated by comma(,):")
        else:
            print("Thank you! your order will be on your table Shortly")
    elif str(sop)=="no" or str(isel)=="NO" or str(isel)=="No":
        morder=input("Pls mention your item/s seperated by comma(,):")
elif str(isel)=="SOUPS" or str(isel)=="Soups" or str(isel)=="soups":
    sorder=input("Pls mention your item/s seperated by comma(,):")
    mop=input("Do you want any MEALS:(type YES/NO)")
    if str(mop)=="yes" or str(mop)=="YES" or str(mop)=="Yes":
        morder=input("Pls mention your item/s seperated by comma(,):")
    else:
        print("Thank you! your order will be on your table Shortly")
elif str(isel)=="Meals" or str(isel)=="meals" or str(isel)=="MEALS":
    morder=input("Pls mention your item/s seperated by comma(,):")
print("your Final order is\n-------"+str(storder)+"-------,\n"+str(sorder)+"---------,\n----------"+str(morder)+"----------.")
print("Thank you! your order will be on your table Shortly")
    
    
    
        
    
    


