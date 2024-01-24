---
title: Programming ADSI with Java/COM
description: Using the Microsoft virtual machine for Java (Microsoft VM) and Microsoft Java Compiler, you have access to all the ADSI features exposed through any ADSI COM components, from a Java/COM application.
ms.assetid: eda516b6-0f89-464f-a9d2-9bb4ca70fda5
ms.tgt_platform: multiple
keywords:
- Programming ADSI with Java/COM AD
- ADSI ADSI , using, Java/COM programming for
- ADSI ADSI , example code Java
- ADSI ADSI , example code Java , binding to an ADSI object and invoking methods on that object
ms.topic: article
ms.date: 05/31/2018
---

# Programming ADSI with Java/COM

Using the Microsoft virtual machine for Java (Microsoft VM) and Microsoft Java Compiler, you have access to all the ADSI features exposed through any ADSI COM components, from a Java/COM application. The following Java code example shows the elements necessary to bind to an ADSI object and invoke methods on that object. The required ADSI API functions and object methods are exposed through Activeds.dll.


```C++
import activeds.*;       // ADSI COM Wrapper classes
import com.ms.com.*;     // to use _Guid data type in COM.

public Class SimpleADSI 
{
    IADs obj;
    String path = "WinNT://domain/machine,computer";
    _Guid riid = IADs.iid;
    public static void main(String args[]) 
    {
        try 
        {
            obj = (IADs)ADsGetObject(path, riid);
            System.out.println( "Object name:  " + obj.getName() );
            System.out.println( "      class:  " + obj.getSchema() );
            System.out.println( "    ADsPath:  " + obj.getADsPath() );
            System.out.println( "     parent:  " + obj.getParent() );
        }
        catch (Exception e) 
        {
            System.out.println( "SimpleADSI Error: " + e.toString() );
        }
    }

    /** @dll.import("activeds", ole) */
    private static native IUnknown ADsGetObject(String path, _Guid riid);
}
```



The argument in the first **import** statement refers to Java Wrapper classes packaged in Activeds.dll. Use Visual J++ to create the wrapper classes and include them in your project, following the procedure below.

**To create wrapper classes and include them in your project**

1.  In a Visual J++ project, select **Add Com Wrapper...** from the **Project** menu.
2.  Select "Active DS Type Library" from the **Installed Components:** from the COM Wrappers dialog. If the type library is not shown in the list box, click the **Browse...** button, navigate to the directory where Activeds.tlb is stored, and then select the type library.

Visual J++ creates the activeds package for the Java Wrapper classes and include the package into the project's default path. For more information, see the activeds package in the **Project Explore** pane on the Visual J++ window.

To get an ADSI object that cannot be cocreated, use one of the exposed ADSI API functions, for example, [**ADsGetObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetobject) or [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject), which are also packaged in Activeds.dll. Microsoft J/Direct provides access to these and other native APIs. This is illustrated by the last two lines of the code example, above.

When compiling, ensure that Microsoft Language Extension is enabled. To do this, select **&lt;project&gt; Properties...** from the **Project** menu in the Visual J++ project window. Then, click the **Compile** tab in the **&lt;project&gt; Properties** dialog. Clear the **Disable Microsoft Language Extensions** check box. If compiling from the command line, use "/x-" switch, for example:

**jvc /x- SimpleADSI.java**

Finally, in order for the virtual machine to load the COM component, the dynamic-link library (DLL) must be visible on the system path. If a "java.lang.UnsatisfiedLinkError" error is returned, set the PATH to include the path that contains the required DLL. For example, if Activeds.dll has been installed in c:\\adsi\\lib, issue the following command from the command line:

**set PATH = %PATH%; c:\\adsi\\lib**

 

 




