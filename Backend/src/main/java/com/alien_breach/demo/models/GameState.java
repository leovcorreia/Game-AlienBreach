package com.alien_breach.demo.models;

public class GameState {

    private Long gameId;
    private Player player;
    private Integer lives;
    private Integer score;
    private Integer level;
    private Double pelletsCollected;
    private String screen;
    private boolean isGameOver;

    public GameState() {
    }

    public GameState(Long gameId, Player player, Integer lives, Integer score, Integer level, Double pelletsCollected, String screen, boolean isGameOver) {
        this.gameId = gameId;
        this.player = player;
        this.lives = lives;
        this.score = score;
        this.level = level;
        this.pelletsCollected = pelletsCollected;
        this.screen = screen;
        this.isGameOver = isGameOver;
    }

    public Long getGameId() {
        return gameId;
    }

    public void setGameId(Long gameId) {
        this.gameId = gameId;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

    public Integer getLives() {
        return lives;
    }

    public void setLives(Integer lives) {
        this.lives = lives;
    }

    public Integer getScore() {
        return score;
    }

    public void setScore(Integer score) {
        this.score = score;
    }

    public Integer getLevel() {
        return level;
    }

    public void setLevel(Integer level) {
        this.level = level;
    }

    public Double getPelletsCollected() {
        return pelletsCollected;
    }

    public void setPelletsCollected(Double pelletsCollected) {
        this.pelletsCollected = pelletsCollected;
    }

    public boolean isGameOver() {
        return isGameOver;
    }

    public void setGameOver(boolean gameOver) {
        isGameOver = gameOver;
    }

    public String getScreen() {
        return screen;
    }

    public void setScreen(String screen) {
        this.screen = screen;
    }

}
