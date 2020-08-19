---
title: Creating a Ribbon Application
description: The Windows Ribbon framework is composed of two distinct, yet dependent, development platforms a markup language based on Extensible Application Markup Language (XAML) to declare controls and their visual layout, and a C++ Component Object Model (COM)-based set of interfaces to define command functionality and application hooks. This division of labor within the Ribbon framework architecture requires that a developer who wants to take advantage of the rich UI capabilities offered by the framework must design and describe the UI in markup, and then use the Ribbon framework COM interfaces to connect the framework to the host application.
ms.assetid: 1bd3dbb5-822b-4551-8330-8b202a4cecdf
keywords:
- Windows Ribbon,creating applications
- Ribbon,creating applications
- Windows Ribbon,roadmap
- Ribbon,roadmap
- Windows Ribbon,markup
- Ribbon,markup
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Ribbon Application

The Windows Ribbon framework is composed of two distinct, yet dependent, development platforms: a markup language based on Extensible Application Markup Language (XAML) to declare controls and their visual layout, and a C++ Component Object Model (COM)-based set of interfaces to define command functionality and application hooks. This division of labor within the Ribbon framework architecture requires that a developer who wants to take advantage of the rich UI capabilities offered by the framework must design and describe the UI in markup, and then use the Ribbon framework COM interfaces to connect the framework to the host application.

-   [Ribbon Roadmap](#ribbon-roadmap)
-   [Write the Markup](#write-the-markup)
    -   [Compile the Markup](#compile-the-markup)
-   [Build the Application](#build-the-application)
    -   [Initialize the Ribbon](#initialize-the-ribbon)
    -   [Link the Markup to the Application](#link-the-markup-to-the-application)
    -   [Compile the Application](#link-the-markup-to-the-application)
-   [Run Time Updates and Executions](#run-time-updates-and-executions)
-   [OLE Support](#ole-support)
-   [Related topics](#related-topics)

## Ribbon Roadmap

The visual aspects of a Ribbon application, such as what controls are displayed and where they are placed, are declared in markup (see [Declaring Commands and Controls with Ribbon Markup](windowsribbon-schema.md)). The application command logic, such as what happens when a button is pressed, is implemented in code.

The process of implementing a Ribbon and incorporating it into a Windows application requires four basic tasks: write the markup, compile the markup, write the code, and compile and link the entire application.

The following diagram illustrates the workflow for a typical Ribbon implementation.

![diagram showing the workflow for a typical ribbon implementation.](images/overviews/ribbonroadmap.png)

The following sections describe this process in more detail.

## Write the Markup

After the Ribbon UI has been designed, the first task for an application developer is to describe the UI with Ribbon markup.

> [!IMPORTANT]
> The Ribbon framework markup schema file, UICC.xsd, is installed with the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0. Using the standard installation path, the file is located in the %ProgramFiles%\\Microsoft SDKs\\Windows\\\[version number\]\\Bin folder where it can be referenced by many XML editors to provide hinting and auto-completion.

 

Ribbon controls, Ribbon Commands (the control-independent elements that provide the base functionality for Ribbon controls), and all control layout and visual relationships are declared in markup. The structure of the Ribbon markup emphasizes the distinction between Ribbon controls and Commands through two primary node hierarchies: a [Commands and Resources](windowsribbon-reference-elements-command.md) tree and a [Views](windowsribbon-reference-elements-view.md) tree.

All containers and actions that are exposed by the Ribbon are declared in the [Commands and Resources](windowsribbon-reference-elements-command.md) tree. Each Command element is associated with a set of resources, as required by the UI design.

After you create the Commands for an application, you declare controls in the [Views](windowsribbon-reference-elements-view.md) tree and bind each control to a Command to expose the Command functionality. The Ribbon framework determines the actual positioning of the controls based on the Control hierarchy declared here.

The following code example illustrates how to declare a Button control, labeled Exit application, and associate it with an Exit Command.


```
<Application xmlns="http://schemas.microsoft.com/windows/2009/Ribbon">
  <Application.Commands>
    <Command Name="cmdExit" LabelTitle="Exit application" />
  </Application.Commands>

  <Application.Views>
    <Ribbon>
      <Ribbon.Tabs>
        <Tab>
          <Group>
            <Button CommandName="cmdExit" />
          </Group>
        </Tab>
      </Ribbon.Tabs>
    </Ribbon>
  </Application.Views>
</Application>
        
```



> [!TIP]
> While it is possible to use any file name extension for the Ribbon markup file, .xml is the recommended extension that is used throughout the documentation.

 

### Compile the Markup

After the Ribbon markup file is created, it must be compiled into a binary format by the Ribbon markup compiler, UI Command Compiler (UICC), that is included with the Windows software development kit (SDK). A reference to this binary file is passed to the [**IUIFramework::LoadUI**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-loadui) method during initialization of the Ribbon framework by the host application.

UICC can be executed directly from a command-line window or added as a "Custom Build Step" in Visual Studio.

The following image shows the UICC markup compiler in the Windows 7 SDK CMD Shell window.

![screen shot showing uicc.exe in a command-line window.](images/overviews/screenshot-intentcl-commandline.png)

The following image shows UICC added as a Custom Build Step in Visual Studio.

![screen shot showing uicc.exe added as a custom build step in visual studio.](images/overviews/screenshot-vs-intentcl-custombuildstep.png)

The UICC generates three files: a binary version of the markup (.bml), an ID definition header (.h file) to expose markup elements to the Ribbon host application, and a [resource-definition script](../menurc/about-resource-files.md) (.rc file) to link Ribbon image and string resources to the host application at compile time.

For more detail on compiling Ribbon framework markup, see [Compiling Ribbon Markup](windowsribbon-intentcl.md).

## Build the Application

Once the preliminary UI for a Ribbon application has been designed and implemented in markup, application code must be written that initializes the framework, consumes the markup, and binds the Commands declared in the markup to the appropriate Command handlers in the application.

> [!IMPORTANT]
>
> Since the Ribbon framework is COM-based, it is recommended that Ribbon projects use the \_\_uuidof() operator to reference the GUIDs for Ribbon framework interfaces (IIDs). In those cases where it is not possible to use the \_\_uuidof() operator, such as when a non-Microsoft compiler is used or the host application is C-based, the IIDs must be defined by the application since they are not contained in uuid.lib.
>
> If the IIDs are defined by the application then the GUIDs specified in UIRibbon.idl must be used.
>
> UIRibbon.idl ships as part of the [Windows Software Development Kit (SDK)](https://msdn.microsoft.com/windows/bb980924.aspx) and can be found at the standard installation path of %ProgramFiles%\\Microsoft SDKs\\Windows\\v7.0\\Include.

 

### Initialize the Ribbon

The following diagram illustrates the steps required to implement a simple Ribbon application.

![diagram showing the steps required to implement a simple ribbon implementation.](images/overviews/initializationsteps.png)

The following steps describe in detail how to implement a simple Ribbon application.

1.  CoCreateInstance

    The application calls the standard COM CoCreateInstance function with the Ribbon framework class ID to obtain a pointer to the framework.

    ```
    IUIFramework* pFramework = NULL;
    HRESULT hr = ::CoCreateInstance(
                CLSID_UIRibbonFramework, 
                NULL,
                CLSCTX_INPROC_SERVER, 
                IID_PPV_ARGS(&pFramework));
    if (FAILED(hr))
    {
      return hr;
    }
    ```

    

2.  Initialize(hwnd, IUIApplication\*)

    The application calls [**IUIFramework::Initialize**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-initialize), passing in two parameters: the handle to the top-level window that will contain the Ribbon and a pointer to the [**IUIApplication**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiapplication) implementation that allows the framework to make callbacks to the application.

    > \[!Important\]  
    > The Ribbon framework is initialized as a single-threaded apartment (STA).

     

    ```
    hr = pFramework->Initialize(hWndHost, pApplication);
    if (FAILED(hr))
    {
      return hr;
    }
    ```

    

3.  LoadUI(instance, resourceName)

    The application calls [**IUIFramework::LoadUI**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-loadui) to bind the markup resource. The first parameter of this function is a handle to the Ribbon application instance. The second parameter is the name of the binary markup resource that was compiled previously. By passing the binary markup to the Ribbon framework, the application signals what the Ribbon structure should be and how controls should be arranged. It also provides the framework with a manifest of commands to expose (such as Paste, Cut, Find), which are used by the framework when it makes Command-related callbacks at run time.

    ```
    hr = pFramework->LoadUI(GetModuleHandle(NULL), L"APPLICATION_RIBBON");
    if (FAILED(hr))
    {
      return hr;
    }
    ```

    

4.  [**IUIApplication::OnCreateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiapplication-oncreateuicommand) callbacks

    After steps 1 through 3 are completed, the Ribbon framework knows which Commands to expose in the Ribbon. However, the framework still needs two things before the Ribbon is fully functional: a way to tell the application when Commands are executed and a way to get Command resources, or properties, at run time. For example, if a combo box is to appear in the UI, then the framework needs to ask for the items with which to populate the combo box.

    These two pieces of functionality are handled through the [**IUICommandHandler**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicommandhandler) interface. Specifically, for each command declared in the binary markup (see Step 3 above), the framework calls [**IUIApplication::OnCreateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiapplication-oncreateuicommand) to ask the application for an **IUICommandHandler** object for that command

    > [!Note]  
    > The [**IUICommandHandler**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicommandhandler) interface allows a Command handler to be bound to one or more Commands.

     

At a minimum, the application is required to implement [**IUIApplication**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiapplication) methods stubs that return E\_NOTIMPL as shown in the following example.


```
STDMETHOD(OnViewChanged)(UINT32 viewId,
                         UI_VIEWTYPE typeID,
                         IUnknown *view,
                         UI_VIEWVERB verb,
                         INT32 uReasonCode)
{ 
  return E_NOTIMPL; 
}

STDMETHOD(OnCreateUICommand)(UINT32 commandId,
                             UI_COMMANDTYPE typeID,
                             IUICommandHandler **commandHandler)
{ 
  return E_NOTIMPL; 
}

STDMETHOD(OnDestroyUICommand)(UINT32 commandId,
                              UI_COMMANDTYPE typeID,
                              IUICommandHandler *commandHandler) 
{ 
  return E_NOTIMPL; 
}
```



### Link the Markup to the Application

At this point, the markup resource files must be linked to the host application by including a reference to the markup resource-definition file (which contains a reference to the markup header file) in the application resource file. For example, an application called RibbonApp with a resource file called ribbonUI.rc requires the following line in the RibbonApp.rc file.


```C++
#include "ribbonUI.rc"
```



Depending on the compiler and linker being used, the resource-definition script may also require compiling before the Ribbon application can be compiled. The [resource compiler (RC)](../menurc/using-rc-the-rc-command-line-.md) command line tool that ships with Microsoft Visual Studio and the Windows SDK can be used for this task.

### Compile the Application

Once the Ribbon application is compiled, it can be run and the UI tested. If the UI requires tweaking and there are no changes to any associated Command handlers in the core application code, revise the markup source file, recompile the markup with UICC.exe, and link the new markup resource files. When the application is restarted, the modified UI is displayed.

All this is possible without touching the core application code—a significant improvement over standard application development and distribution.

## Run Time Updates and Executions

The run-time communication structure of the Ribbon framework is based on a push and pull, or two-way caller, model.

This model allows the framework to inform the application when a Command is executed and allows both the framework and the application to query, update, and invalidate property values and Ribbon resources. This functionality is provided through a number of interfaces and methods.

The framework pulls updated property information from the Ribbon application through the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method. A Command ID and a property key, which identifies the Command property to update, are passed to the method which then returns, or pushes, a value for that property key to the framework.

The framework calls [**IUICommandHandler::Execute**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-execute) when a Command is executed, identifying both the Command ID and the type of execution that occurred ([**UI\_EXECUTIONVERB**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_executionverb)). This is where the application specifies the execution logic for a command.

The following diagram illustrates the run-time communication for Command execution between the framework and the application.

![diagram showing an example of the run-time communication between the ribbon framework and a host application.](images/overviews/updatesandexecutions.png)

> [!Note]  
> Implementing the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) and [**IUICommandHandler::Execute**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-execute) functions is not necessary to initially display a Ribbon in an application. However, these methods are necessary to ensure that the application functions correctly when commands are executed by the user.

 

## OLE Support

A Ribbon application can be configured as an OLE server to support out-of-place OLE activation.

Objects created in an OLE server application maintain their association with the server application when inserted (either pasted or placed) into an OLE client application (or container). In out-of-place OLE activation, double clicking the object in the client application opens a dedicated instance of the server application and loads the object for editing. When the server application is closed, all changes made to the object are reflected in the client application.

> [!Note]  
> The Ribbon framework does not support in-place OLE activation. Objects created in a Ribbon-based OLE server cannot be edited from within the OLE client application. An external dedicated instance of the server application is required.


## Related topics

<dl> <dt>

[Declaring Commands and Controls with Ribbon Markup](./windowsribbon-schema.md)
</dt> <dt>

[Ribbon User Experience Guidelines](https://msdn.microsoft.com/library/cc872782.aspx)
</dt> <dt>

[Ribbon Design Process](https://msdn.microsoft.com/library/cc872781.aspx)
</dt> </dl>

 

 




