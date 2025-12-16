const statusEl = document.getElementById("status");
const infoUsernameEl = document.getElementById("info-username");
const userDetailsEl = document.getElementById("user-details");
const historyEl = document.getElementById("history");

const loginMsgEl = document.getElementById("login-msg");
const registerMsgEl = document.getElementById("register-msg");

const loginUsernameEl = document.getElementById("login-username");
const loginPasswordEl = document.getElementById("login-password");

const regUsernameEl = document.getElementById("reg-username");
const regEmailEl = document.getElementById("reg-email");
const regPasswordEl = document.getElementById("reg-password");

let users = JSON.parse(localStorage.getItem("users") || "[]");
let historyData = JSON.parse(localStorage.getItem("history") || "[]");
let currentUser = null;

document.querySelectorAll(".tab").forEach(tab => {
    tab.addEventListener("click", () => {
        document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
        document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));

        tab.classList.add("active");
        document.getElementById(tab.dataset.tab).classList.add("active");
    });
});

function showMessage(element, text, type) {
    element.textContent = text;
    element.className = "message " + type;
    element.style.display = "block";

    setTimeout(() => {
        element.style.display = "none";
    }, 3000);
}

function register() {
    const username = regUsernameEl.value.trim();
    const email = regEmailEl.value.trim();
    const password = regPasswordEl.value;

    if (!username || !email || password.length < 6) {
        showMessage(registerMsgEl, "Мэдээлэл буруу байна", "error");
        return;
    }

    const exists = users.some(u => u.username === username);
    if (exists) {
        showMessage(registerMsgEl, "Хэрэглэгч аль хэдийн бүртгэлтэй байна", "error");
        return;
    }

    users.push({
        username: username,
        email: email,
        password: btoa(password)
    });

    localStorage.setItem("users", JSON.stringify(users));
    showMessage(registerMsgEl, "Амжилттай бүртгэгдлээ", "success");

    regUsernameEl.value = "";
    regEmailEl.value = "";
    regPasswordEl.value = "";
}

// ===== LOGIN FUNCTION =====
function login() {
    const username = loginUsernameEl.value.trim();
    const password = loginPasswordEl.value;

    const user = users.find(
        u => u.username === username && u.password === btoa(password)
    );

    const statusText = user ? "Амжилттай" : "Амжилтгүй";

    historyData.unshift({
        time: new Date().toLocaleString(),
        username: username,
        status: statusText
    });

    historyData = historyData.slice(0, 5);
    localStorage.setItem("history", JSON.stringify(historyData));

    if (!user) {
        showMessage(loginMsgEl, "Нэр эсвэл нууц үг буруу", "error");
        return;
    }

    currentUser = user;
    updateUI();
    showMessage(loginMsgEl, "Амжилттай нэвтэрлээ", "success");

    loginUsernameEl.value = "";
    loginPasswordEl.value = "";
}

function updateUI() {
    statusEl.textContent = "Нэвтэрсэн";
    statusEl.className = "logged-in";

    infoUsernameEl.textContent = currentUser.username;
    userDetailsEl.style.display = "block";

    historyEl.innerHTML = "";
    historyData.forEach(h => {
        historyEl.innerHTML += `
            <tr>
                <td>${h.time}</td>
                <td>${h.username}</td>
                <td>${h.status}</td>
            </tr>
        `;
    });
}

function logout() {
    currentUser = null;

    statusEl.textContent = "Нэвтрээгүй";
    statusEl.className = "logged-out";
    userDetailsEl.style.display = "none";
}