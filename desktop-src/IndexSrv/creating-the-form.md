---
title: Creating the Form
description: Creating the Form
ms.assetid: 4ba6f404-9eb2-4e5d-98cc-558321810a98
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating the Form

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

After you have set up the header, you are ready to create the .asp search form.


```
<TABLE>
    <TR>
        <TD><H1>Sample ASP Search Form</H1></TD>
    </TR>
</TABLE>
 
<HR WIDTH=75% ALIGN=center SIZE=3>
<p>
 
<TABLE>
  <TR>
    <TD ALIGN=LEFT>Enter your query below:</TD>
  </TR>
  <TR>
    <TD>
      <FORM ACTION="<%= QueryForm%>" METHOD=POST>
 
        <TABLE>
          <TR>
            <TD><INPUT TYPE="TEXT" NAME="SearchString" SIZE="60"
                         MAXLENGTH="100" VALUE="<%=SearchString%>"></TD>
            <TD><INPUT TYPE="SUBMIT" NAME="Action" VALUE="New Query"></TD>
          </TR>
        </TABLE>
       
      </FORM>
    </TD>
  </TR>
</TABLE>
```



The two most important lines are the FORM ACTION and the INPUT TYPE lines.

<dl> <dt>

<span id="_FORM_ACTION._._._"></span><span id="_form_action._._._"></span>&lt;FORM ACTION. . .&gt;
</dt> <dd>

This line names the current file, where the processing code is located.

</dd> <dt>

<span id="_INPUT_TYPE__TEXT_._._._"></span><span id="_input_type__text_._._._"></span>&lt;INPUT TYPE="TEXT". . .&gt;
</dt> <dd>

Here the variable *SearchString* is preset to accept whatever text is typed in the "Enter your query below" field. For example, if you type "cache" in this field, *SearchString* holds the text "cache".

</dd> <dt>

<span id="_INPUT_TYPE__SUBMIT_._._._"></span><span id="_input_type__submit_._._._"></span>&lt;INPUT TYPE="SUBMIT". . .&gt;
</dt> <dd>

This line creates the button that executes your query. In this example, the button is called **New Query**.

</dd> </dl>

 

 




