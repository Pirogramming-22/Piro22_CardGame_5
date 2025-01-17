function generateRanking() {
    const userDataElements = document.querySelectorAll("#user-data li");
    const users = Array.from(userDataElements).map(el => ({
        username: el.dataset.username,
        points: parseInt(el.dataset.points, 10)
    }));

    const barContainer = document.getElementById("bar-container");
    const rankingList = document.getElementById("ranking-list");

    // 최대 점수 계산 (막대 높이 비율을 정하기 위해 사용)
    const maxPoints = Math.max(...users.map(user => user.points), 0);

    users.sort((a, b) => b.points - a.points);

    let currentRank = 1; 
    let lastScore = null; 
    const minBarHeight = 10; 

    users.forEach((user, index) => {
        if (user.points !== lastScore) {
            currentRank = index + 1;
        }

        const bar = document.createElement("div");
        bar.className = `bar bar${index + 1}`;

        // 막대 높이 계산
        let barHeight = (user.points / maxPoints) * 100;
        barHeight = Math.max(barHeight, minBarHeight); 

        bar.style.height = `${barHeight}%`;

        bar.innerHTML = `${currentRank}위`;

        barContainer.appendChild(bar);

        const rank = document.createElement("p");
        rank.textContent = `${currentRank}위: ${user.username} (${user.points}점)`;
        rankingList.appendChild(rank);

       
        lastScore = user.points;
    });
}

generateRanking();