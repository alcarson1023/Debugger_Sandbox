import React, { useState } from "react";

const App = () => {
  const [text, setText] = useState("");
  const [processedText, setProcessedText] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    fetch("/api/process", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({text}),
    })
      .then((response) => response.json())
      .then((data) => {
        setProcessedText(data.processed_text);
        console.log(data);
      })
      .catch((error) => {
        // Handle errors
        console.error(error);
      });
  };



  //   try {
  //     console.log('JS text = ', text)
  //     const response = await fetch('/api/process', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //       },
  //       body: JSON.stringify({ text }),
  //     });

  //     console.log(response)

  //     if (!response.ok) {
  //       throw new Error('An error occurred while processing the text.');
  //     }

  //     const data = await response.json();
  //     setProcessedText(data.processed_text);
  //   } catch (error) {
  //     console.error(error);
  //   }
  // };

  return (
    <div>
      <h1>React Example</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="text">Enter text: </label>
        <input
          type="text"
          id="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
      {processedText && <p>Processed Text: {processedText}</p>}
    </div>
  );
};

export default App;
