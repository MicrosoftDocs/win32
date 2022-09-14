---
description: This topic identifies several error-handling strategies to keep in mind as you develop components for COM+.
ms.assetid: 1ae5875b-8085-44f2-9071-c2a5d7543ac1
title: Strategies for Handling Errors in COM+
ms.topic: article
ms.date: 05/31/2018
---

# Strategies for Handling Errors in COM+

This topic identifies several error-handling strategies to keep in mind as you develop components for COM+.

-   **Return an HRESULT value for all methods in all component interfaces.**  COM+ uses **HRESULT** values to report on any errors in making function calls or interface method calls. An **HRESULT** indicates whether a method succeeded or failed and identifies the facility associated with the error, such as RPC, WIN32, or ITF for interface-specific errors. Also, system APIs provide a lookup from an **HRESULT** to a string that describes the error condition. Using methods that return **HRESULT** values are fundamental to well-written components and are essential to the debugging process. Microsoft Visual Basic automatically defines each method with an **HRESULT** as a return. In Microsoft Visual C++, you must explicitly return an **HRESULT**. For additional information on HRESULTs, see [Structure of COM Error Codes](/windows/desktop/com/structure-of-com-error-codes).
-   **Initiate the ErrorInfo collection object by whatever means your development tool provides.** [**ErrorInfo**](errorinfo.md) collection objects are often called COM exceptions because they allow an object to pass (or throw) rich error information to its caller, even across apartment boundaries. The value of this generic error object is that it supplements an HRESULT, extending the type of error information that you can return to a caller. Each **ErrorInfo** collection object returns a contextual description, the source of the error, and the interface identifier of the method that originated the error. You can also include pointers to an entry in a help file. Automation provides three interfaces to manage the error object. Your component must implement the **ISupportErrorInfo** Automation interface to advertise its support for the **ErrorInfo** collection. When an error occurs, the component uses the **ICreateErrorInfo** Automation interface to initialize an error object. After the caller inspects the HRESULT and finds that the method call failed, it queries the object to see whether it supports the **ErrorInfo** collection. If it does, the caller uses the **IErrorInfo** Automation interface to retrieve the error information. Visual Basic programmers have easy access to the **ErrorInfo** collection object, which is exposed through the Err object. You can raise errors with the Err Raise function and catch errors with the **On Error** statement. The Visual Basic run-time layer takes care of the mapping for you. If you are using the Visual C++ COM compiler support, you can use the \_com\_raise\_error class to report an error and the \_com\_error class to retrieve error information. COM+ will not propagate traditional C++ exceptions as extended **IErrorInfo** information. For additional information on the **ErrorInfo** collection object, see "Error Handling" in the Automation guide.
    > [!Note]  
    > COM requires that all [**ErrorInfo**](errorinfo.md) collection objects marshal by value, implying that components that implement the **IErrorInfo** Automation interface must also implement and support the [**IMarshal**](/windows/desktop/api/objidl/nn-objidl-imarshal) interface. The **IMarshal** interface implementation must support marshal by value for the component.

     

-   **Use transactions to manage shared resource failures.** Automatic transactions can significantly reduce the amount of error-handling code you must write when using state-managed resource managers. However, transactions do not eliminate the need for error handling altogether. You still need to return error codes from your interface methods and check those error codes within the caller to avoid doing unnecessary work for a doomed transaction. For additional information about combining error handling with transaction processing, see [Speeding Transactions by Notifying the Root Object](speeding-transactions-by-notifying-the-root-object.md).
-   **Raise errors explicitly.** Avoid letting error information leave an object unless the object explicitly raises the error. Catch all tool-generated errors and handle them in your component code. At the very least, include a standard handler to report unexpected errors in a consistent manner.
-   **Use the FACILITY\_ITF range of errors to report interface-specific errors.** Interface-specific errors should be in the FACILITY\_ITF range of errors, between 0x0200 and 0xFFFF. You can define a custom error code in Visual Basic as an offset from vbObjectError. Use the MAKE\_HRESULT macro in C++ to introduce an interface-specific error code, as shown in the following example:

    ``` syntax
    const HRESULT ERROR_NUMBER = MAKE_HRESULT (SEVERITY_ERROR, FACILITY_ITF, 10);
    ```

## Related topics

<dl> <dt>

[Fault Isolation and Failfast Policy](fault-isolation-and-failfast-policy.md)
</dt> <dt>

[Finding the Source of an Error](finding-the-source-of-an-error.md)
</dt> <dt>

[How COM+ Modifies Return Values](how-com--modifies-return-values.md)
</dt> <dt>

[Interpreting Error Codes](interpreting-error-codes.md)
</dt> <dt>

[Troubleshooting](troubleshooting.md)
</dt> </dl>

 

 
