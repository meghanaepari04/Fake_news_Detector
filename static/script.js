document.getElementById("predictForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const newsInput = document.getElementById("newsInput").value.trim();
  const resultElement = document.getElementById("result");

  if (!newsInput) {
    resultElement.textContent = "⚠️ Please enter some text.";
    return;
  }

  resultElement.textContent = "⏳ Checking...";

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: newsInput })
    });

    const data = await response.json();
    resultElement.textContent = data.prediction;
  } catch (error) {
    resultElement.textContent = "❌ Error connecting to server!";
    console.error(error);
  }
});
