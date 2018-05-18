---
title: defaultcollelem
description: Allows for optimization of code.
ms.assetid: '8c402244-7fb1-4fb6-b11c-c983fae82cb2'
---

# defaultcollelem

Allows for optimization of code.

## Allowed on

Property, members in dispinterfaces and interfaces.

## Flags

<dl> FUNCFLAG\_FDEFAULTCOLLELEM  
VARFLAG\_FDEFAULTCOLLELEM  
</dl>

## Remarks

In Visual Basic for Applications (VBA5.0), " MyForm!myProp" is normally syntactic shorthand for MyForm.defaultprop("myProp"). Because such a call is significantly slower than accessing a data member of MyForm directly, an optimization has been added in which the compiler looks for a member named "myProp " on the type of MyForm. If such a member is found and flagged as an accessor function for an element of the default collection, a call is generated to that member function.

Because this optimization searches the type of item that precedes the '!', it will optimize calls of the form MyForm!myProp only if MyForm has a member named " myProp", and it will optimize MyForm.Controls! myProp only if the return type of Controls has a member named myProp. Even though MyForm!myProp and MyForm.Controls!myProp both would normally generate the same calls to the object server, optimizing these two forms requires that the object server add the myProp method in both places.

Use of \[defaultcollelem\] must be consistent for a property. For example, if it is present on a **Get**, it must also be present on a **Put**.

## Example

A form has a button on it named "Button1". User code can access the button using property syntax or ! syntax, as shown below.


```C++
Sub Test()
   Dim f As Form1
   Dim b1 As Button
   Dim b2 As Button

   Set f = Form1

   Set b1 = f.Button1     ' Property syntax
   Set b = f!Button1      ' ! syntax
End Sub
```



To use the property syntax and the ! syntax properly, see the form in the type information below.


```C++
   [  odl, 
      dual,
      uuid(1e196b20-1f3c-1096-996b-00dd010ef676),
      helpstring("This is IForm"),
      restricted
   ]
   interface IForm1: IForm
   {
      [propget, defaultcollelem]
      HRESULT Button1([out, retval] Button *Value);
   }
```



## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




