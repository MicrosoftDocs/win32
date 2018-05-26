---
title: Specifying Search Filters
description: The definition of the search filter query syntax for DSML V2 is part of the DSML V2 XML schema specification. The following syntax is derived from LDAP search filter strings as defined in RFC 2254, but is significantly different.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0bf52e8b-62eb-4ac8-b882-c18cc6cbba8c
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Specifying Search Filters DSML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Specifying Search Filters

The definition of the search filter query syntax for DSML V2 is part of the DSML V2 XML schema specification. The following syntax is derived from LDAP search filter strings as defined in RFC 2254, but is significantly different.

The following code examples show typical LDAP search strings and their DSML V2 equivalents.

## Find all objects in the directory

LDAP Filter

``` syntax
    (objectclass=*)
```

DSML V2 Filter

``` syntax
    <filter>
      <present name="objectclass"/>
    </filter>
```

## Find all contacts with a 'sn' that starts with 'J'

LDAP Filter

``` syntax
    (&(objectCategory=contact)(sn=J*))
```

DSML V2 Filter

``` syntax
    <filter>
      <and>
        <equalityMatch name="objectCategory">
          <value>contact</value>
        </equalityMatch>   
        <substrings name="sn">                                                       
          <initial>J</initial>                    
        </substrings>
      </and>
    </filter>
```

## Find all 'organizationalUnit' objects with a description that contains the literal string 'H\*Q'

LDAP Filter

``` syntax
    (&(objectCategory=organizationalUnit)(description=H\2aQ))
```

DSML V2 Filter

``` syntax
    <filter>
      <and>
        <equalityMatch name="objectCategory">
          <value>organizationalUnit</value>
        </equalityMatch>   
        <equalityMatch name="description">                                                       
          <value>H*Q</value>                    
        </equalityMatch>
      </and>
    </filter>
```

## Find all 'inetorgpersons' objects whose room number is between 2000 and 3000 inclusively

LDAP Filter

``` syntax
    (&(objectClass=inetorgperson)(roomnumber>=2000)(roomnumber<=3000))
```

DSML V2 Filter

``` syntax
    <filter>
      <and>
        <equalityMatch name="objectClass">
          <value>inetorgperson</value>
        </equalityMatch>
        <greaterOrEqual name="roomnumber">
          <value>2000</value> 
        </greaterOrEqual>
        <lessOrEqual name="roomnumber">
          <value>3000</value> 
        </lessOrEqual>
      </and>
    </filter>
```

## Find all objects that do not have an assistant

LDAP Filter

``` syntax
    (!(assistant=*))
```

DSML V2 Filter

``` syntax
    <filter>
      <not>
        <present name="assistant"/>  
      </not>
    </filter>
```

## Find all 'user' objects in 'departmentNo 101' that do not have an assistant

LDAP Filter

``` syntax
    (&(objectCategory=person)(objectClass=user)(departmentNo=101)(!(assistant=*)))
```

DSML V2 Filter

``` syntax
    <filter>
      <and>
        <equalityMatch name="objectCategory">
          <value>person</value>
        </equalityMatch>   
        <equalityMatch name="objectClass">
          <value>user</value>
        </equalityMatch>   
        <equalityMatch name="departmentNo">
          <value>101</value>
        </equalityMatch>   
        <not>
          <present name="assistant"/>  
        </not>
      </and>
    </filter>
```

## Find all 'organizationalUnit' objects that have a description equal to &lt;Marketing-Central&gt;

LDAP Filter

``` syntax
    (&(objectClass=organizationalUnit)(description=<Marketing-Central>))
```

DSML V2 Filter

``` syntax
    <filter>
      <and>
        <equalityMatch name="objectClass">
          <value>organizationalUnit</value>
        </equalityMatch>   
        <equalityMatch name="description">
          <value>&lt;Marketing-Central&gt;</value>
        </equalityMatch>   
      </and>
    </filter>
```

## Find all 'organizationalUnit' objects that have a description equal to (Marketing-Central)

LDAP Filter

``` syntax
    (&(objectClass=organizationalUnit)(description=\28Marketing-Central\29))
```

DSML V2 Filter

``` syntax
    <filter>
      <and>
        <equalityMatch name="objectClass">
          value>organizationalUnit</value>
        </equalityMatch>   
        <equalityMatch name="description">
          <value>(Marketing-Central)</value>
        </equalityMatch>   
      </and>
    </filter>
```

## Find all objects with a 'bin' attribute value equal to 'a\\00a'

This value is a three-byte binary value, where the first byte is the ASCII value of 'a', the second byte is 0x00, and the third is 'a', that is, {'a',0x00,'a'}.

LDAP Filter

``` syntax
    (bin=a\00a)
```

DSML V2 Filter

``` syntax
    <filter>
      <equalityMatch name="bin">
        <value xsi:type="xsd:base64Binary">YQBh</value>         
      </equalityMatch>   
    </filter>
```

## Matching rules

LDAP Filter

``` syntax
    (&(objectCategory=attributeSchema)(systemFlags:1.2.840.113556.1.4.804:=1))
```

DSML V2 Filter

``` syntax
    <filter>
      <and>
        <equalityMatch name="objectCategory">
          <value>attributeSchema</value>         
        </equalityMatch>   
        <extensibleMatch name="systemFlags" matchingRule="1.2.840.113556.1.4.804">
          <value>1</value>  
        </extensibleMatch>
      </and>
    </filter>
```

 

 




