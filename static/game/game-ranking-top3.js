
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

    // 막대와 랭킹 생성
    users.forEach((user, index) => {
        
        const bar = document.createElement("div");
        bar.className = `bar bar${index + 1}`;
        const barHeight = Math.max((user.points / maxPoints) * 100, 0); 
        bar.style.height = `${barHeight}%`;
        bar.innerHTML = `${user.username}<br>${user.points}`;

        
        barContainer.appendChild(bar);

        // 랭킹 리스트 생성
        const rank = document.createElement("p");
        rank.textContent = `${index + 1}위: ${user.username} (${user.points}점)`;
        rankingList.appendChild(rank);
    });
}


generateRanking();
