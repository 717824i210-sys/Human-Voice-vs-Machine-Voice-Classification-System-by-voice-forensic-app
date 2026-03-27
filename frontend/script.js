document.getElementById("uploadBtn").addEventListener("click", async () => {
  const fileInput = document.getElementById("fileInput");
  if (!fileInput.files.length) {
    alert("Please select a file first!");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    body: formData
  });

  const result = await response.json();
  document.getElementById("result").innerHTML = `
    <p><b>Prediction:</b> ${result.prediction}</p>
    <p><b>Confidence:</b> ${result.confidence}</p>
  `;
});