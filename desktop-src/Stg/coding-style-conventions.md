---
title: Coding Style Conventions
description: Coding style conventions are used in this sample series to aid clarity and consistency.
ms.assetid: d5e81a52-79f6-4561-891c-05fee125a1b0
ms.topic: article
ms.date: 05/31/2018
---

# Coding Style Conventions

Coding style conventions are used in this sample series to aid clarity and consistency. The "Hungarian" notation conventions are used. These have become a common coding practice in Win32 programming. They include variable prefix notations that give to variable names a suggestion of the type of the variable.

The following table lists common prefixes.



| Prefix | Description                         |
|--------|-------------------------------------|
| a      | Array                               |
| b      | BOOL (int)                          |
| c      | Char                                |
| cb     | Count of bytes                      |
| cr     | Color reference value               |
| cx     | Count of x (short)                  |
| dw     | DWORD (unsigned long)               |
| f      | Flags (usually multiple bit values) |
| fn     | Function                            |
| g\_    | Global                              |
| h      | Handle                              |
| i      | Integer                             |
| l      | Long                                |
| lp     | Long pointer                        |
| m\_    | Data member of a class              |
| n      | Short int                           |
| p      | Pointer                             |
| s      | String                              |
| sz     | Zero terminated String              |
| tm     | Text metric                         |
| u      | Unsigned int                        |
| ul     | Unsigned long (ULONG)               |
| w      | WORD (unsigned short)               |
| x,y    | x, y coordinates (short)            |



 

These are often combined, as in the following.



| Prefix combination | Description                                             |
|--------------------|---------------------------------------------------------|
| pszMyString        | A pointer to a string.                                  |
| m\_pszMyString     | A pointer to a string that is a data member of a class. |



 

Other conventions are listed in the following table.



| Convention       | Description                                              |
|------------------|----------------------------------------------------------|
| CMyClass         | Prefix 'C' for C++ class names.                          |
| COMyObjectClass  | Prefix 'CO' for COM object class names.                  |
| CFMyClassFactory | Prefix 'CF' for COM class factory names.                 |
| IMyInterface     | Prefix 'I' for COM interface class names.                |
| CImpIMyInterface | Prefix 'CImpI' for COM interface implementation classes. |



 

Some consistent conventions for comment header blocks are used in this sample series as follows.

## File Header

``` syntax
/*+===================================================================
  File:      MYFILE.EXT

  Summary:   Brief summary of the file contents and purpose.

  Classes:   Classes declared or used (in source files).

  Functions: Functions exported (in source files).

  Origin:    Indications of where content may have come from. This
             is not a change history but rather a reference to the
             editor-inheritance behind the content or other
             indications about the origin of the source.

  Copyright and Legal notices.
  Copyright and Legal notices.
===================================================================+*/
```

## Plain Comment Block

``` syntax
/*--------------------------------------------------------------------
  Plain block of comment text that usually takes several lines.
  Plain block of comment text that usually takes several lines.
--------------------------------------------------------------------*/
```

## Class Declaration Header

``` syntax
/*C+C+++C+++C+++C+++C+++C+++C+++C+++C+++C+++C+++C+++C+++C+++C+++C+++C
  Class:    CMyClass

  Summary:  Short summary of purpose and content of CMyClass.
            Short summary of purpose and content of CMyClass.

  Methods:  MyMethodOne
              Short description of MyMethodOne.
            MyMethodTwo
              Short description of MyMethodTwo.
            CMyClass
              Constructor.
            ~CMyClass
              Destructor.
C---C---C---C---C---C---C---C---C---C---C---C---C---C---C---C---C-C*/
```

## Class Method Definition Header

``` syntax
/*M+M+++M+++M+++M+++M+++M+++M+++M+++M+++M+++M+++M+++M+++M+++M+++M+++M
  Method:   CMyClass::MyMethodOne

  Summary:  Short summary of purpose and content of MyMethodOne.
            Short summary of purpose and content of MyMethodOne.

  Args:     MYTYPE MyArgOne
              Short description of argument MyArgOne.
            MYTYPE MyArgTwo
              Short description of argument MyArgTwo.

  Modifies: [list of member data variables modified by this method].

  Returns:  MYRETURNTYPE
              Short description of meaning of the return type values.
M---M---M---M---M---M---M---M---M---M---M---M---M---M---M---M---M-M*/
```

## Unexported or Local Function

``` syntax
/*F+F+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  Function: MyLocalFunction

  Summary:  What MyLocalFunction is for and what it does.

  Args:     MYTYPE MyFunctionArgument1
              Description.
            MYTYPE MyFunctionArgument1
              Description.

  Returns:  MyReturnType
              Description.
-----------------------------------------------------------------F-F*/
```

## Exported Function Definition Header

``` syntax
/*F+F+++F+++F+++F+++F+++F+++F+++F+++F+++F+++F+++F+++F+++F+++F+++F+++F
  Function: MyFunction

  Summary:  What MyFunction is for and what it does.

  Args:     MYTYPE MyFunctionArgument1
              Description.
            MYTYPE MyFunctionArgument1
              Description.

  Returns:  MyReturnType
              Description.
F---F---F---F---F---F---F---F---F---F---F---F---F---F---F---F---F-F*/
```

## COM Interface Declaration Header

``` syntax
/*I+I+++I+++I+++I+++I+++I+++I+++I+++I+++I+++I+++I+++I+++I+++I+++I+++I
  Interface: IMyInterface

  Summary:   Short summary of what features the interface can bring to
             a COM Component.

  Methods:   MYTYPE MyMethodOne
               Description.
             MYTYPE MyMethodTwo
               Description.
I---I---I---I---I---I---I---I---I---I---I---I---I---I---I---I---I-I*/
```

## COM Object Class Declaration Header

``` syntax
/*O+O+++O+++O+++O+++O+++O+++O+++O+++O+++O+++O+++O+++O+++O+++O+++O+++O
  ObjectClass: COMyCOMObject

  Summary:     Short summary of purpose and content of this object.

  Interfaces:  IUnknown
                 Standard interface providing COM object features.
               IMyInterfaceOne
                 Description.
               IMyInterfaceTwo
                 Description.

  Aggregation: [whether this COM Object is aggregatable or not]
O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O-O*/
```

All of these comment block conventions have consistent beginning and ending token strings. This consistency supports automatic processing of the headers in some fashion. For example, AWK scripts can be written to filter the function headers into a separate text file that can then serve as the basis for a specification document. Similarly, tools like the unsupported AUTODUCK utility (currently available on the Microsoft Developer Network Development Library CD-ROM) can be used to process the comment blocks in these headers.

The following table lists beginning and ending token strings used in sample tutorials.



| Token | Description                      |
|-------|----------------------------------|
| /\*+  | File Header Begin                |
| +\*/  | File Header End                  |
| /\*-  | Plain comment block Header Begin |
| -\*/  | Plain comment block Header End   |
| /\*C  | Class Header Begin               |
| C\*/  | Class Header End                 |
| /\*M  | Method Header Begin              |
| M\*/  | Method Header End                |
| /\*F  | Function Header Begin            |
| F\*/  | Function Header End              |
| /\*I  | Interface Header Begin           |
| I\*/  | Interface Header End             |
| /\*O  | COM Object Class Header Begin    |
| O\*/  | COM Object Class Header End      |



 

These headers can also be used as visual cues for rapid scanning of source files. They also provide convenience for rapidly getting to some source location if you set up search strings in your editor and then 'repeat last search' to quickly locate these headers.

For example, the search string "M+M" will locate the start of method headers, and "M-M" will locate the beginning of the actual method definition/implementation code.

 

 




