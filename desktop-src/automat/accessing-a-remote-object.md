---
title: Accessing a Remote Object
description: Demonstrates how to access a remote object.
ms.assetid: '826dbe0d-7bd1-4b70-9d15-4de3a97a8db2'
---

# Accessing a Remote Object

With Visual Basic, accessing a remote object requires only that the program declare an object variable and assign the return of a **New** statement to the variable.

The following is the syntax for the statements:


```C++
Dim ObjectVar As InterfaceName
Set ObjectVar = New CoClassName
```



The **Dim** statement declares a variable of an interface type. The **New** keyword creates an instance of an object. Used together, the two declare and create an instance of an ActiveX object. For example:


```C++
Dim MyLines As ILines
Set MyLines = New Lines.Lines
```



The **Dim** statement declares the object variable MyLines of the interface type **ILines**. The **Set** statement assigns a new object of the *component object class* (coclass) Lines to the variable MyLines. When you use the **Dim** statement to set a variable to an interface type, subsequent uses of the variable will execute faster than with the generic Object syntax.

The **New** keyword applies only to creating coclasses of interface or dispinterface types. To create other types of objects, the variable must be declared with the **Dim** statement, and the **CreateObject** function used as follows:


```C++
Set ObjectVar = CreateObject(ProgID)
```



**CreateObject** creates an ActiveX object, based on the specified programmatic identifier (ProgID). The ProgID has the form:


```C++
AppName.ObjectName
```



The *AppName* is the name of the application, and the *ObjectName* identifies the type of object to create. For more information about ProgIDs, see [Registering the Application](registering-the-application.md) in [Exposing ActiveX Objects](exposing-activex-objects.md).

You can use the **GetObject** function to re-establish the reference to the most recently used object that corresponds to the *Filename* and *AppName*.*ObjectName* specification, as follows:


```C++
Set ObjectVar = GetObject("Filename", ProgID)
```



For example, if the ActiveX client needs an existing instance of an object instead of a new instance, it can use the **GetObject** function.

The Hello sample application, included in the Platform Software Development Kit (SDK), displays a Hello message in response to a mouse click. You can add a simple form that accesses the Hello application's exposed object from another process.

### To add a form

1.  Start Visual Basic.

2.  Click **Open Project** on the **File** menu.

3.  In the dialog box, click Vb.mak in the Sample directory.

4.  In the **Forms** box, click **View Form** to see the form, or click **View Code** to see the Visual Basic code.

    ```C++
    Module-level declarations
    Dim HelloObj As IHello

    Sub Form_load ( )
       Set HelloObj = New Hello.Hello
    End Sub

    Sub Invoke_SayHello_Method_Click ( )
       HelloObj.SayHello
    End Sub

    Sub Get_HelloMsg_Property_Click ()
       Debug.Print HelloObj.HelloMessage
    End Sub

    Sub Set_HelloMsg_Property_Click ( )
       HelloObj.HelloMessage = "Hello Universe"
    End Sub

    Sub SetVisible_Click ( )
       HelloObj.Visible = True
    End Sub
    ```

    

The Form\_Load subroutine creates the Hello Application object. Other subroutines manipulate the Hello Application object through the **Visible** and HelloMessage properties and the SayHello method.

To program an object in Visual Basic, you need its class name and the names and parameters of its properties and methods. For the Hello sample application, you need to know the exact names of the SayHello method, and the **Visible** and HelloMsg properties, along with the types of their arguments. This information is provided in the documentation for many objects, such as those exposed by Microsoft Excel. You can also get the information by viewing the object's type library with an object browser, such as the one included in Visual Basic.

 

 




