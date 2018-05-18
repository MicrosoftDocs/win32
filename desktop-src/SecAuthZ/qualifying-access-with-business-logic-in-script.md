---
Description: 'Using business rule scripts in Script to provide run-time logic for checking access.'
ms.assetid: '10c28ecb-3f36-45a8-b037-7038e8927b6b'
title: Qualifying Access with Business Logic in Script
---

# Qualifying Access with Business Logic in Script

Use business rule scripts to provide run-time logic for checking access. For more information about business rules, see [Business Rules](business-rules.md).

To assign a business rule to a task, first set the [**BizRuleLanguage**](iaztask-bizrulelanguage.md) property of the [**IAzTask**](iaztask.md) object that represents the task. The script must be written using the Visual Basic Scripting Edition (VBScript) programming language or JScript development software. After you specify the script language, set the [**BizRule**](iaztask-bizrule.md) property of the **IAzTask** object with a string representation of the script.

When checking access for an operation contained by a task that has an associated business rule, the application must create two arrays of the same size to be passed as the *varParameterNames* and *varParameterValues* parameters of the [**AccessCheck**](iazclientcontext-accesscheck.md) method of an [**IAzClientContext**](iazclientcontext.md) object. For information about creating a client context, see [Establishing a Client Context in Script](establishing-a-client-context-in-script.md).

The [**AccessCheck**](iazclientcontext-accesscheck.md) method creates an [**AzBizRuleContext**](azbizrulecontext.md) object that is passed to the business rule script. The script then sets the [**BusinessRuleResult**](azbizrulecontext-businessruleresult.md) property of the **AzBizRuleContext** object. A value of **True** indicates that access is granted, and a value of **False** indicates that access is denied.

A business rule script cannot be assigned to an [**IAzTask**](iaztask.md) object contained by a delegated [**IAzScope**](iazscope.md) object.

The following example shows how to use a business rule script to check a client's access to an operation. The example assumes that there is an existing XML policy store named MyStore.xml in the root directory of drive C, and that this store contains an application named Expense, a task named Submit Expense, and an operation named UseFormControl.


```VB
<%@ Language=VBScript %>
<%
'  Create the AzAuthorizationStore object.
Dim AzManStore
Set AzManStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the authorization store.
AzManStore.Initialize 0, "msxml://C:\MyStore.xml"

'  Open the application object in the store.
Dim expenseApp
Set expenseApp = AzManStore.OpenApplication("Expense")

'  Create a client context.
Dim clientName
clientName = Request.ServerVariables("LOGON_USER")
Dim clientContext
Set clientContext = _
    expenseApp.InitializeClientContextFromName(clientName)

'  Create a business rule for the Submit Expense task.

'  Open the Submit Expense task.
Dim submitTask
Set submitTask = expenseApp.OpenTask("Submit Expense")

'  Set the business rule language to VBScript.
submitTask.BizRuleLanguage = "VBScript"

'  Create a string with the business rule code.
Dim newline
newline = chr(13)
Dim bizRuleString
bizRuleString = "Dim Amount" + newline _
         +"AzBizRuleContext.BusinessRuleResult = FALSE" + newline _
         +"Amount = AzBizRuleContext.GetParameter(""ExpAmount"")" _
   +newline _
   +"if Amount < 500 then AzBizRuleContext.BusinessRuleResult = TRUE"

'  Assign the business rule to the Submit Expense task.
submitTask.BizRule = bizRuleString
                
'  Save the task information to the store.
submitTask.Submit

'  Open the operation to check.
Dim formOperation
Set formOperation = expenseApp.OpenOperation("UseFormControl")

'  Get the ID of the operation.
Dim operationID
operationID = formOperation.OperationID

'  Set up arrays for operations and results.
Dim Operations(1)
Operations(0) = operationID
Dim Results

'  Set up business rule parameters.
Dim bizNames(1)
Dim bizValues(1)
bizNames(0) = "ExpAmount"
bizValues(0) = 100

'  Check access.
Results = clientContext.AccessCheck _
    ("UseFormControl", Empty, Operations, bizNames, bizValues)
 
%>
```



 

 



