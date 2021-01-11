---
description: To create an application dictionary, it is necessary to set the WordList property of the RecognizerContext object.
ms.assetid: 24dbf617-fa16-44f1-ba59-d4d99b8f1375
title: Using an Application Dictionary with InkEdit
ms.topic: article
ms.date: 05/31/2018
---

# Using an Application Dictionary with InkEdit

To create an application dictionary, it is necessary to set the [**WordList**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist) property of the [**RecognizerContext**](inkrecognizercontext-class.md) object. The [InkEdit](inkedit-control-reference.md) control does not expose the **RecognizerContext** object, so it is not possible to directly set the **WordList** property of the InkEdit control's **RecognizerContext** object.

To use an application dictionary with an [InkEdit](inkedit-control-reference.md) control, you must take the strokes out of the InkEdit control, pass them to a new [**RecognizerContext**](inkrecognizercontext-class.md) object with the [**WordList**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist) property set to a [**WordList**](inkwordlist-class.md) containing the application dictionary, store the results from this **RecognizerContext** object, and then pass the results back to the InkEdit control.

## Example

The following C\# code shows an example of this technique.


```C++
private RecognizerContext rc;
private WordList wl;
private int wlSelStart;
private int wlSelLen;
private bool isRecoPending = false;

private void Form1_Load(object sender, EventArgs e)
{
  //event handlers must be attached for dictionary to work.
  inkEdit1.Recognition += new Microsoft.Ink.InkEditRecognitionEventHandler(inkEdit1_Recognition);
  inkEdit1.TextChanged += new EventHandler(inkEdit1_TextChanged);

  //create a WordList that contains the application dictionary
  wl = new WordList();
  //...
  //Add dictionary terms to the WordList
  //...

  // create a RecognizerContext for the WordList
  rc = inkEdit1.Recognizer.CreateRecognizerContext();
  rc.Factoid = Factoid.WordList;

  //set the RecognizerContext WordList to the newly created WordList
  rc.WordList = wl;

  //create a delegate for the new RecognizerContext
  rc.RecognitionWithAlternates += new

  RecognizerContextRecognitionWithAlternatesEventHandler(rc_Recognition);
}

void inkEdit1_TextChanged(object sender, EventArgs e)
{
  if (isRecoPending)
  {
    isRecoPending = false;
    rc.BackgroundRecognizeWithAlternates();
  }
}

private void inkEdit1_Recognition(object sender,
Microsoft.Ink.InkEditRecognitionEventArgs e)
{
  //store the start of the selection in wlSelStart
  wlSelStart = inkEdit1.SelectionStart;

  //store the length of the selection in wlSelLen
  wlSelLen = e.RecognitionResult.TopString.Length;

  //copy the strokes from the InkEdit control into the new
  // RecognizerContext
  rc.Strokes = e.RecognitionResult.Strokes.Ink.Clone().Strokes;
  isRecoPending = true;
}

private void rc_Recognition(object sender,
Microsoft.Ink.RecognizerContextRecognitionWithAlternatesEventArgs e)
{
  if (inkEdit1.InvokeRequired)
  {
    inkEdit1.Invoke(new RecognizerContextRecognitionWithAlternatesEventHandler(rc_Recognition),
      new object[] { sender, e });
    return;
  }

  //set the insertion point in the InkEdit control
  inkEdit1.SelectionStart = wlSelStart;
  inkEdit1.SelectionLength = wlSelLen;
  //insert the result from the new RecognizerContext 
  //into the InkEdit control
  inkEdit1.SelectedText = e.Result.TopString;
  inkEdit1.SelectionStart = inkEdit1.SelectionStart +
  e.Result.TopString.Length;
}

// Event handler for the form's closed event
private void Form1_Closed(object sender, System.EventArgs e)
{
  inkEdit1.Dispose();
  inkEdit1 = null;
  rc.Dispose();
  rc = null;
}
```



## Related topics

<dl> <dt>

[InkEdit Control](/previous-versions/ms552265(v=vs.100))
</dt> <dt>

[Microsoft.Ink.RecognizerContext Class](/previous-versions/ms552546(v=vs.100))
</dt> <dt>

[Microsoft.Ink.Wordlist Class](/previous-versions/ms827589(v=msdn.10))
</dt> </dl>

 

 
