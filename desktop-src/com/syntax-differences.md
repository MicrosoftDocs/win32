---
title: Syntax Differences
description: The most apparent change as you move between programming languages is the change in syntax.
ms.assetid: 179efb69-3794-4a06-b770-2b3dc8409172
ms.topic: article
ms.date: 05/31/2018
---

# Syntax Differences

The most apparent change as you move between programming languages is the change in syntax.

Consider the EnhEvents object's Add method, shown as it is declared in three different languages.

``` syntax
object.Add(Time As Double, Name As String) As Variant

HRESULT Add(
  double Time, 
  BSTR Name, 
  VARIANT* pVal
);
 
public com.ms.com.Variant Add( 
  double Time, 
  java.lang.String Name
);
 
```

Although the syntax of each language expresses the method differently, the functionality is the same. In each language, the Add method takes the parameters *Time* and *Name* and returns an EnhEvent object. In the C++ example, the method returns the object by using a third, output parameter, *pVal*.

Typically, the functionality of a COM object is the same across programming languages. Because of this, documentation for a COM object is useful even if the object is documented in another programming language than the one you are using. The descriptions of the object's functionality, parameters, and return values are, with few exceptions, valid for all languages.

For information about how to convert the syntax of a COM object to another programming language, see [Translating COM Object Syntax for Programming Languages](translating-com-object-syntax-for-programming-languages.md).

The syntax differences among the scripting languages JavaScript, JScript, and VBScript are less pronounced than the syntax differences among the programming languages shown preceding. For example, consider the square function as it is implemented in each of these three scripting languages:

``` syntax
Function square(x)
  square = x*x
End Function
 
function square(x){ return x*x; }
 
function square(x){ return x*x; }
 
```

Notice that the scripting languages, unlike the programming languages, are weakly typed. In other words, you do not have to specify the data type of a parameter or return value when you declare a function. Instead, the variables are automatically cast to the appropriate data type. In the case of VBScript, all variables are of the same data type, **Variant**.

The JavaScript and JScript syntax for square is the same. JScript is largely compatible with JavaScript. However, JScript includes some objects not currently supported by JavaScript, such as **ActiveXObject**, **Enumerator**, **Error**, **Global**, and **VBArray**. For more information about these objects, see the [JScript Language Reference](/previous-versions/visualstudio/visual-studio-2010/ye921ye4(v=vs.100)).

On the surface, JavaScript and JScript syntax resembles Java syntax. This similarity is only superficial. The Java language was developed independently from both JavaScript and JScript and is not related to either.

VBScript, on the other hand, is a subset of the Visual Basic programming language. Because of this, VBScript syntax is a subset of Visual Basic syntax and is often interchangeable with Visual Basic syntax.

For information on using COM objects in scripting languages, see [Scripting with COM Objects](scripting-with-com-objects.md).

 

 